from forno_eletrico import forno_gpio
import time

forno = forno_gpio()

forno.setup()

def ligar_forno():
    forno.ligado = not forno.ligado

def set_temp_180():
    forno.temp = 180

def set_temp_210():
    forno.temp = 210

def set_temp_250():
    forno.temp = 250

while (1):
    time.sleep(0.1)
    entrada = forno.read_button()
    print("\n\nBotão pressionado: ", entrada)

    if entrada == 1:
        print("\n\nLiga/Desliga forno: ", entrada)
        ligar_forno()
    elif entrada == 2:
        print("\n\nSeta a temperatura para 180: ", entrada)
        set_temp_180()
    elif entrada == 3:
        print("\n\nSeta a temperatura para 210: ", entrada)
        set_temp_210()
    elif entrada == 4:
        print("\n\nSeta a temperatura para 250: ", entrada)
        set_temp_250()
    elif entrada == 5:
        print("\n\nOpção desabilitada: ", entrada)
        forno.setup()



