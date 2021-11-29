import time
import math as m

def myDecorator(functionToDecorate):
    def wrapperAroundTheOriginalFunction():
        print(f"Была вызвана функция: {functionToDecorate}")
        functionToDecorate()
        print(f"Время, затраченное на выполнение функции: {time.perf_counter()}")
    return wrapperAroundTheOriginalFunction()

lengthInFeet = int(input("Введите длину в футах: "))
widthInFeet = int(input("Введите ширину в футах: "))

@myDecorator
def calculateArea():
    SQFT_PER_ACRE = (lengthInFeet * widthInFeet) * 0.000023
    print(f'Участок c длиной {lengthInFeet} футов и шириной {widthInFeet} футов, имеет площадь {SQFT_PER_ACRE} акров')

height = int(input('Высота с которой будет брошен объект: '))
defaultSpeed = 0
gravity = 9.8

@myDecorator
def findSpeed():
    finalSpeed = m.sqrt(m.pow(defaultSpeed, 2) + 2 * (gravity*height))
    print(f'Скорость в точке соприкосновения с землей равна {finalSpeed}')