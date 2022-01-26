result = ''
q = int(input("Введите число для преобразования "))
r = 0

while q > 0:
    result = str(q % 2) + result
    q = q // 2

print(result)