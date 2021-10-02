#Program for testing processor
#
#Russian Laung
import os

from time import sleep
from random import randint

print('Чем больше числа тем дольше они будут угадыватся')
a = int(input('Число от: '))
b = int(input('До: '))
c = int(input('Хотите чтобы вам показывались неудачные попытоки?\n1)Да\n2)Нет\n'))
i = 0

while True:
    randomNumber = randint(a, b)
    randomUgad = randint(a, b)

    if (c == 1):
        if(randomUgad == randomNumber):
        i += 1
        print(f'{randomUgad} = {randomNumber}\nУгадано число за {i} попыток')
        break
        if(randomUgad < randomNumber):
            i += 1
            print(f'{randomUgad} < {randomNumber}')
        if(randomUgad > randomNumber):
            i += 1
            print(f'{randomUgad} > {randomNumber}')
    if(c == 2):
        if(randomUgad == randomNumber):
        i += 1
        print(f'{randomUgad} = {randomNumber}\nУгадано число за {i} попыток')
        break
    else:
        os.system('python app.py')
