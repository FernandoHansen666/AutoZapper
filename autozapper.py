import pywhatkit as pwk
import datetime
import time


number = ["+numero","+numero"] 
mensagem = 'Isto é um teste, se recebeu significa que meu Algoritimo em python esta feito com sucesso!'

i = 0

while i < len(number):
    now = datetime.datetime.now()

    pwk.sendwhatmsg_instantly(number[i], mensagem, 10, True, 3)

    i + 1
    time.sleep(3)

