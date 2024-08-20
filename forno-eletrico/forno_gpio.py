import random
import time
import RPi.GPIO as GPIO

# Botões
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

def read_button():
	while (not (GPIO.input(liga_desliga) or GPIO.input(temp_180) or GPIO.input(temp_250) or GPIO.input(opc_desabilitado) or GPIO.input(seleciona_tempo))):
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
	GPIO.output(liga_desliga, GPIO.LOW)
	GPIO.output(temp_180, GPIO.LOW)
	GPIO.output(temp_220, GPIO.LOW)
	GPIO.output(temp_250, GPIO.LOW)
	GPIO.output(opc_desabilitado, GPIO.LOW)
	GPIO.output(seleciona_tempo, GPIO.LOW)

def setup():
	GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme

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
	leds_off()

def main():
	setup()

if __name__ == '__main__':
	try:
		main()
	except SystemExit as e:
		print("Program aborted")
		raise e
	finally:
		GPIO.cleanup()