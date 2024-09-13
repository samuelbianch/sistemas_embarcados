import RPi.GPIO as GPIO
import time

# Definição dos pinos de saída (LEDs)
resistencia = 5  # GPIO 5  | Saída
exaustor = 26    # GPIO 26 | Saída

# Definição do pino de entrada (botão)
botao_toggle = 3  # GPIO 3 | Entrada

# Estado inicial dos LEDs
led_resistencia_ligado = False
led_exaustor_ligado = False

# Função de configuração
def setup():
    GPIO.setmode(GPIO.BCM)  # Usar a numeração de pinos BCM do Raspberry Pi

    # Configuração dos pinos como saída
    GPIO.setup(resistencia, GPIO.OUT)
    GPIO.setup(exaustor, GPIO.OUT)

    # Configuração do pino do botão como entrada com pull-down resistor
    GPIO.setup(botao_toggle, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    # Inicializa os LEDs como desligados
    GPIO.output(resistencia, GPIO.LOW)
    GPIO.output(exaustor, GPIO.LOW)

    print("Pinos configurados.")

# Função para alternar os LEDs
def alternar_leds():
    global led_resistencia_ligado, led_exaustor_ligado

    # Se o LED de resistência está ligado, desligue-o e ligue o LED de exaustor
    if led_resistencia_ligado:
        GPIO.output(resistencia, GPIO.LOW)
        GPIO.output(exaustor, GPIO.HIGH)
        led_resistencia_ligado = False
        led_exaustor_ligado = True
        print("LED Exaustor ON, LED Resistência OFF")
    # Caso contrário, ligue o LED de resistência e desligue o LED de exaustor
    else:
        GPIO.output(resistencia, GPIO.HIGH)
        GPIO.output(exaustor, GPIO.LOW)
        led_resistencia_ligado = True
        led_exaustor_ligado = False
        print("LED Resistência ON, LED Exaustor OFF")

# Função principal
def main():
    setup()

    try:
        while True:
            # Verifica se o botão foi pressionado
            if GPIO.input(botao_toggle) == GPIO.HIGH:
                alternar_leds()  # Alterna os LEDs
                time.sleep(0.3)  # Debounce para evitar múltiplos acionamentos
            time.sleep(0.1)  # Pequena espera para aliviar a CPU

    except KeyboardInterrupt:
        print("Interrupção do teclado detectada. Limpando pinos GPIO.")
        GPIO.cleanup()

# Executa o programa principal
if __name__ == '__main__':
    main()
