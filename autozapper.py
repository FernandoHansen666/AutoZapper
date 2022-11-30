import pywhatkit as pwk
import datetime
import time



number = "+554396286759"
mensagem = 'Isto é um teste, se recebeu significa que meu Algoritimo em python esta feito com sucesso!'

i = 1

while i < 6:
    now = datetime.datetime.now()
    pwk.sendwhatmsg_instantly(
        number, mensagem, 10, True, 3
    )
    i + 1
    time.sleep(3)
