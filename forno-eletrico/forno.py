import RPi.GPIO as GPIO

import time

# GPIO Pin Definitions
liga_desliga = 5        # GPIO 3    | Entrada
temp_180 = 11           # GPIO 17   | Entrada
temp_220 = 13           # GPIO 27   | Entrada
temp_250 = 15           # GPIO 22   | Entrada
opc_desabilitado = 21   # GPIO 9   | Entrada
seleciona_tempo = 19    # GPIO 10    | Entrada

# LEDs
resistencia = 29        # GPIO 5    | Saída
forno_ligado = 31       # GPIO 6    | Saída
aquecendo = 33          # GPIO 13   | Saída
resfriando = 35         # GPIO 19   | Saída
exaustor = 37           # GPIO 26   | Saída

temp = 27 # Variavel para representar a Temperatura ambiente

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
    GPIO.output(exaustor, GPIO.HIGH)
    leds_off()

def read_button():
    while (not (GPIO.input(liga_desliga) or GPIO.input(temp_180) or GPIO.input(temp_220) or GPIO.input(temp_250) or GPIO.input(opc_desabilitado) or GPIO.input(seleciona_tempo))):
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

def ligar_desligar_forno():
    forno_ligado = not forno_ligado
    if forno_ligado:
        GPIO.output(forno_ligado, GPIO.HIGH)
    else:
        GPIO.output(forno_ligado, GPIO.LOW)
        setup()

def set_temperatura(temperatura_setada):
    if forno_ligado:
        if temp < temperatura_setada:
            resistencia = 1
            GPIO.output(resistencia, GPIO.HIGH)
            GPIO.output(resfriando, GPIO.HIGH)
            while temp < temperatura_setada:
                temp += 1
                time.sleep(0.1)
            resistencia = 0
            GPIO.output(resistencia, GPIO.LOW)
        else:
            GPIO.output(resistencia, GPIO.LOW)
            GPIO.output(resfriando, GPIO.HIGH)
            while temp > temperatura_setada:
                temp -= 1
                time.sleep(0.1)
            GPIO.output(resfriando, GPIO.LOW)
    else:
        pass

def desabilita():
    if forno_ligado:
        GPIO.output(exaustor, GPIO.HIGH)
        time.sleep(3)
        setup()
    else:
        pass


def selecionando_tempo():
    if forno_ligado:
        # Essa implementação funcionará da seguinte maneira
        # 1. O usuário pressiona o botão de selecionar tempo
        # 2. O usuário pressiona o botão de aumentar tempo
        # 3. A cada vez que ele aperta o botão em um intervalo de 3 segundos, o tempo é adicionado
        # Exemplo: pressiono para selecionar o tempo, o contador começa
        # presiono em um intervalo de 3 segundos, o botão mais 3 vezes, então o tempo setado é: 120.
        # Faça um timer de 3 segundos
        tempo = 0
        tempo_setado = 30
        while tempo < 3:
            if read_button() == 6:
                tempo_setado += 30
            time.sleep(0.1)
            tempo += 0.1
        print("\n\nTempo setado: ", tempo_setado)
    else:
        pass

def verifica_temperatura_maior_40_graus():
    if temp > 40:
        GPIO.output(aquecendo, GPIO.HIGH)
    else:
        GPIO.output(aquecendo, GPIO.LOW)


def main():
    setup()

    while (True):
        GPIO.output(resistencia, GPIO.HIGH)
        time.sleep(10)
        verifica_temperatura_maior_40_graus()
        entrada = read_button()
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

#if __name__ == '__main__':
#    try:
#        print("teste")
#        main()
#    except Exception as e:
#            print(f"Abortado: {e}")
#    finally:
#        GPIO.cleanup()

main()
