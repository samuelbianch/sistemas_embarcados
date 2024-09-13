import RPi.GPIO as GPIO
import time

# GPIO Pin Definitions
liga_desliga = 3        # GPIO 3    | Entrada
temp_180 = 17           # GPIO 17   | Entrada
temp_220 = 27           # GPIO 27   | Entrada
temp_250 = 22           # GPIO 22   | Entrada
opc_desabilitado = 9   # GPIO 9    | Entrada
seleciona_tempo = 10    # GPIO 10   | Entrada

# LEDs
resistencia = 5         # GPIO 5    | Saída
forno_ligado = 6        # GPIO 6    | Saída
aquecendo = 13          # GPIO 13   | Saída
resfriando = 19         # GPIO 19   | Saída
exaustor = 26           # GPIO 26   | Saída

temp = 27                   # Variável para representar a Temperatura ambiente
forno_ligado_state = False  # Estado do forno
tempo_funcionamento = 30    # Variavel para fornecer o tempo de funcionamento

def setup():
    GPIO.setmode(GPIO.BCM)  # Broadcom pin-numbering scheme

    # Buttons setup as INPUT with pull-down resistors
    GPIO.setup(liga_desliga, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(temp_180, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(temp_220, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(temp_250, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(opc_desabilitado, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(seleciona_tempo, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    # LEDs setup as OUTPUT
    GPIO.setup(resistencia, GPIO.OUT)
    GPIO.setup(forno_ligado, GPIO.OUT)
    GPIO.setup(aquecendo, GPIO.OUT)
    GPIO.setup(resfriando, GPIO.OUT)
    GPIO.setup(exaustor, GPIO.OUT)
    leds_off()

def read_button():
    while (not (GPIO.input(liga_desliga) or GPIO.input(temp_180) or GPIO.input(temp_220) or GPIO.input(temp_250) or GPIO.input(opc_desabilitado) or GPIO.input(seleciona_tempo))):
        time.sleep(0.05)
        pass
    if GPIO.input(liga_desliga):
        return 1
    if GPIO.input(temp_180):
        return 2
    if GPIO.input(temp_220):
        return 3
    if GPIO.input(temp_250):
        return 4
    if GPIO.input(opc_desabilitado):
        return 5
    if GPIO.input(seleciona_tempo):
        return 6

def leds_off():
    GPIO.output(resistencia, GPIO.LOW)
    GPIO.output(forno_ligado, GPIO.LOW)
    GPIO.output(aquecendo, GPIO.LOW)
    GPIO.output(resfriando, GPIO.LOW)
    GPIO.output(exaustor, GPIO.LOW)

def cleanup():
    GPIO.cleanup()

def contar_presses():
    contador = 0
    tempo_ultima_pressao = time.time()
    while True:
        # Verifica se o botão foi pressionado
        if GPIO.input(seleciona_tempo) == GPIO.HIGH:
            contador += 1
            tempo_ultima_pressao = time.time()
            while GPIO.input(seleciona_tempo) == GPIO.HIGH:
                time.sleep(0.05)
        if time.time() - tempo_ultima_pressao > 2:
            break

        time.sleep(0.05)

    return contador

def set_tempo():
    # Essa implementação funcionará da seguinte maneira
    # 1. O usuário pressiona o botão de selecionar tempo
    # 2. O usuário pressiona o botão de aumentar tempo
    # 3. A cada vez que ele aperta o botão em um intervalo de 2 segundos, o tempo é adicionado
    # Exemplo: pressiono para selecionar o tempo, o contador começa
    # presiono em um intervalo de 2 segundos, o botão mais 4 vezes, então o tempo setado é: 120.
    global tempo_funcionamento
    tempo_setado = 0
    while (not (GPIO.input(seleciona_tempo) or GPIO.input(liga_desliga) or GPIO.input(opc_desabilitado))):
        time.sleep(0.05)
        pass
    if GPIO.input(liga_desliga):
        ligar_desligar_forno()
        return 0
    elif GPIO.input(opc_desabilitado):
        desabilita()
        return 0
    elif GPIO.input(seleciona_tempo):
        tempo_setado = ((contar_presses()-1) * 30)
        if tempo_setado > 0:
            if tempo_setado > 120:
                tempo_setado = 120
            print("\n\nTempo setado: ", tempo_setado)
            tempo_funcionamento = tempo_setado
            return tempo_setado
        else:
            print("Forno não iniciado porque você não setou o tempo:")
            time.sleep(0.5)
            print("Set o tempo")
            set_tempo()
            return 0

def ligar_desligar_forno():
    global forno_ligado_state
    forno_ligado_state = not forno_ligado_state
    global tempo_funcionamento
    if forno_ligado_state:
        GPIO.output(forno_ligado, GPIO.HIGH)
    else:
        GPIO.output(forno_ligado, GPIO.LOW)
        main()

def set_temperatura(temperatura_setada):
    global temp, forno_ligado_state, tempo_funcionamento
    tempo_que_ligou = time.time()
    if forno_ligado_state:
        print("\ntemp: ", temp)
        print("\ntemperatura_setada: ", temperatura_setada)
        if temp < temperatura_setada:
            GPIO.output(resistencia, GPIO.HIGH)
            GPIO.output(aquecendo, GPIO.HIGH)
            GPIO.output(resfriando, GPIO.LOW) 
            while (temp < temperatura_setada):
                verifica_temperatura_maior_40_graus()
                print("\ntemp: ", temp)
                print("\ntemperatura_setada: ", temperatura_setada)
                if GPIO.input(opc_desabilitado):
                    desabilita()
                    return "Forno desligado"
                print("Temperatura no forno: ", temp)
                tempo_ligado = time.time() - tempo_que_ligou
                print("\ntempo_ligado: ", tempo_ligado)
                print("\ntempo_funcionamento", tempo_funcionamento)
                if tempo_ligado < tempo_funcionamento:
                    temp += 1
                    time.sleep(0.1)
                else:
                    break
            
            print("Forno ligado aguardando o timer...")
            if (tempo_funcionamento - tempo_funcionamento) > 0:
                time.sleep(tempo_funcionamento - tempo_ligado)
            GPIO.output(resistencia, GPIO.LOW)
            print("Pronto!")
    else:
        pass
    GPIO.output(resistencia, GPIO.LOW)
    GPIO.output(resfriando, GPIO.HIGH)
    while temp > 27:
        verifica_temperatura_maior_40_graus()
        print("Temperatura no forno: ", temp)
        temp -= 10
        time.sleep(0.5)
    GPIO.output(resfriando, GPIO.LOW)
    

def verifica_temperatura_maior_40_graus():
    if temp > 40:
        GPIO.output(aquecendo, GPIO.HIGH)
    else:
        GPIO.output(aquecendo, GPIO.LOW)

def desabilita():
    global temp
    if forno_ligado:
        leds_off()
        GPIO.output(exaustor, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(exaustor, GPIO.LOW)
        temp = 27
    else:
        pass

def main():
    global tempo_funcionamento
    setup()

    while True:
        verifica_temperatura_maior_40_graus()
        entrada = read_button()
        time.sleep(0.1)
        print("\n\nBotão pressionado: ", entrada)

        if entrada == 1:
            print("\n\nLiga/Desliga forno: ", entrada)
            ligar_desligar_forno()
        elif entrada == 2:
            print("\n\nSeta a temperatura para 180: ", entrada)
            set_temperatura(180)
        elif entrada == 3:
            print("\n\nSeta a temperatura para 210: ", entrada)
            set_temperatura(210)
        elif entrada == 4:
            print("\n\nSeta a temperatura para 250: ", entrada)
            set_temperatura(250)
        elif entrada == 5:
            print("\n\nOpção desabilitada: ", entrada)
            desabilita()
        elif entrada == 6:
            print("\n\nSeleciona tempo: ", entrada)
            if set_tempo() > 0:
                tempo_funcionamento 
            else:
                pass 

try:
    main()
except Exception as e:
    print(f"Abortado: {e}")
finally:
    GPIO.cleanup()
