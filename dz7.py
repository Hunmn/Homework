def sis(a, b):
    if b == 2:
        print(bin(a))
    elif b == 16:
        print(hex(a))
    elif b == 8:
        print(oct(a))
    elif b == 10:
        print(int(a))
    else:
        print('Первое-число, Второе-система исчисления')

sis(5,2)
sis(5,16)
sis(5,8)
sis(0b101,10)
