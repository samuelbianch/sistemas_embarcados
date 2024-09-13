import RPi.GPIO as GPIO
import time

# Definição dos pinos de saída (LEDs)
resistencia = 5        # GPIO 5    | Saída
forno_ligado = 6       # GPIO 6    | Saída
aquecendo = 13         # GPIO 13   | Saída
resfriando = 19        # GPIO 19   | Saída
exaustor = 26          # GPIO 26   | Saída

# Definição do pino de entrada (botão)
botao_pausa = 3        # GPIO 3    | Entrada

# Variável de controle para o estado de pausa
pausar = False

# Função de configuração
def setup():
    GPIO.setmode(GPIO.BCM)  # Usar a numeração de pinos BCM do Raspberry Pi

    # Configuração dos pinos como saída
    GPIO.setup(resistencia, GPIO.OUT)
    GPIO.setup(forno_ligado, GPIO.OUT)
    GPIO.setup(aquecendo, GPIO.OUT)
    GPIO.setup(resfriando, GPIO.OUT)
    GPIO.setup(exaustor, GPIO.OUT)

    # Configuração do pino do botão como entrada com pull-down resistor
    GPIO.setup(botao_pausa, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    print("Pinos configurados.")

# Função para alternar o estado de pausa
def alternar_pausa():
    global pausar
    pausar = not pausar  # Alterna o estado de pausa
    print(f"Estado de pausa: {'Pausado' if pausar else 'Rodando'}")

# Função para piscar LEDs
def blink_leds():
    try:
        while True:
            # Verifica se o botão foi pressionado
            if GPIO.input(botao_pausa) == GPIO.HIGH:
                alternar_pausa()  # Alterna o estado de pausa
                time.sleep(0.3)  # Debounce para evitar múltiplos acionamentos

            if not pausar:  # Somente pisca se não estiver em pausa
                # Liga todos os LEDs
                GPIO.output(resistencia, GPIO.HIGH)
                GPIO.output(forno_ligado, GPIO.HIGH)
                GPIO.output(aquecendo, GPIO.HIGH)
                GPIO.output(resfriando, GPIO.HIGH)
                GPIO.output(exaustor, GPIO.HIGH)
                print("LEDs ON")
                time.sleep(1)

                # Desliga todos os LEDs
                GPIO.output(resistencia, GPIO.LOW)
                GPIO.output(forno_ligado, GPIO.LOW)
                GPIO.output(aquecendo, GPIO.LOW)
                GPIO.output(resfriando, GPIO.LOW)
                GPIO.output(exaustor, GPIO.LOW)
                print("LEDs OFF")
                time.sleep(1)
            else:
                time.sleep(0.1)  # Espera curta quando pausado

    except KeyboardInterrupt:
        print("Interrupção do teclado detectada. Limpando pinos GPIO.")
        GPIO.cleanup()

# Função principal
def main():
    setup()
    blink_leds()

if __name__ == '__main__':
    main()
