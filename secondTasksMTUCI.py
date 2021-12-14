import math

# 1 задача
def areaOfRegularPolygon():
    s = int(input("Введите  длину стороны: "))
    n = int(input("Введите количество сторон: "))
    area = (n * (s * s)) / 4 * math.atan(math.pi / n)
    print(area)

areaOfRegularPolygon()

# 2 задача
def sumOfPositiveNumbers():
    n = int(input("Введите положительное число n: "))
    sum = ((n)*(n+1))/2
    print(sum)

sumOfPositiveNumbers()

# 3 задача
def typeOfСharacter():
    char = input("Введите любую букву латинского алфавита: ")
    vowels = ["a", "e", "i", "o", "u"]
    if char == "y":
        print("Буква может быть как гласной, так и согласной")
    elif char in vowels:
        print("Гласная")
    else:
        print("Согласная")

typeOfСharacter()