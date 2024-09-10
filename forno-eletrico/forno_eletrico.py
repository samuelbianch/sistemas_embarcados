import forno_gpio
import time

forno = forno_gpio.Forno()

forno.setup()

def ligar_desligar_forno():
    forno.ligado = not forno.ligado

def set_temperatura(temperatura_setada):
    if forno.temp < temperatura_setada:
        forno.resistencia = 1
        while forno.temp < temperatura_setada:
            forno.temp += 1
            time.sleep(0.1)
        forno.resistencia = 0
    else:
        while forno.temp > temperatura_setada:
            forno.temp -= 1
            time.sleep(0.1)

def seleciona_tempo():
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
        if forno.read_button() == 6:
            tempo_setado += 30
        time.sleep(0.1)
        tempo += 0.1
    print("\n\nTempo setado: ", tempo_setado)

def verifica_temperatura_maior_40_graus():
    if forno.temp > 40:
        forno.aquecendo = 1
    else:
        forno.aquecendo = 0

while (1):
    time.sleep(0.1)
    verifica_temperatura_maior_40_graus()
    entrada = forno.read_button()
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
        forno.setup()
    elif entrada == 6:
        print("\n\nSeleciona tempo: ", entrada)



