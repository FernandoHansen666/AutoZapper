import pywhatkit as pwk
import datetime
import time


number = ["+5515","+5543","+55number"] #numeros na arraylist
mensagem = 'Teste de algoritimo'

i = 0

while i < len(number):
    now = datetime.datetime.now()

    pwk.sendwhatmsg_instantly(number[i], mensagem, 10, True, 3)
    #pwk.sendwhatmsg(number[i], mensagem, 17,26 , 3, True, 3)

    i = i + 1
    time.sleep(3)

