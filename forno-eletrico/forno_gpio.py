import RPi.GPIO as GPIO

class Forno:
    # GPIO Pin Definitions
    liga_desliga = 5        # GPIO 3    | Entrada
    temp_180 = 11           # GPIO 17   | Entrada
    temp_220 = 13           # GPIO 27   | Entrada
    temp_250 = 15           # GPIO 22   | Entrada
    opc_desabilitado = 19   # GPIO 10   | Entrada
    seleciona_tempo = 21    # GPIO 9    | Entrada

    # LEDs
    resistencia = 29        # GPIO 5    | Saída
    forno_ligado = 31       # GPIO 6    | Saída
    aquecendo = 33          # GPIO 13   | Saída
    resfriando = 35         # GPIO 19   | Saída

    def __init__(self):
        self.temp = 27 # Temperatura ambiente
        self.setup()

    def setup(self):
        GPIO.setmode(GPIO.BCM)  # Broadcom pin-numbering scheme

        # Buttons setup as INPUT with pull-down resistors
        GPIO.setup(self.liga_desliga, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.temp_180, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.temp_220, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.temp_250, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.opc_desabilitado, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.seleciona_tempo, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        # LEDs setup as OUTPUT
        GPIO.setup(self.resistencia, GPIO.OUT)
        GPIO.setup(self.forno_ligado, GPIO.OUT)
        GPIO.setup(self.aquecendo, GPIO.OUT)
        GPIO.setup(self.resfriando, GPIO.OUT)
        self.leds_off()

    def read_button(self):
        while (not (GPIO.input(self.liga_desliga) or GPIO.input(self.temp_180) or GPIO.input(self.temp_220) or GPIO.input(self.temp_250) or GPIO.input(self.opc_desabilitado) or GPIO.input(self.seleciona_tempo))):
            pass
        if GPIO.input(self.liga_desliga):
            return 1
        if GPIO.input(self.temp_180):
            return 2
        if GPIO.input(self.temp_220):
            return 3
        if GPIO.input(self.temp_250):
            return 4
        if GPIO.input(self.opc_desabilitado):
            return 5
        if GPIO.input(self.seleciona_tempo):
            return 6

    def leds_off(self):
        GPIO.output(self.resistencia, GPIO.LOW)
        GPIO.output(self.forno_ligado, GPIO.LOW)
        GPIO.output(self.aquecendo, GPIO.LOW)
        GPIO.output(self.resfriando, GPIO.LOW)

    def cleanup(self):
        GPIO.cleanup()

if __name__ == '__main__':
    forno = Forno()
    try:
        # Execute desired functionality here
        pass
    except SystemExit as e:
        print("Program aborted")
        raise e
    finally:
        forno.cleanup()
