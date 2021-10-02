#Program for testing processor
#
#Russian Laung


from time import sleep
from random import randint

print('Чем больше числа тем дольше они будут угадыватся')
a = int(input('Число от: '))
b = int(input('До: '))
i = 0

while True:
    randomNumber = randint(a, b)
    randomUgad = randint(a, b)

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