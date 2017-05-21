#|AB|² = (y2 - y1)² + (x2 - x1)²
x1 = int(input('Введите x1: '))
y1 = int(input('Введите y1: '))
x2 = int(input('Введите x2: '))
y2 = int(input('Введите y2: '))
x3 = int(input('Введите x3: '))
y3 = int(input('Введите y3: '))

dlina1 = (y2 - y1) ** 2 + (x2 - x1) ** 2
dlina2 = (y3 - y2) ** 2 + (x3 - x2) ** 2
dlina3 = (y3 - y1) ** 2 + (x3 - x1) ** 2

if dlina1 + dlina2 == dlina3 or dlina2 + dlina3 == dlina1 or dlina1 + dlina3 ==dlina2:
    print ('Прямоугольный')
else:
    print ('Не прямоугольный')
