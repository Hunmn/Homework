def chet(x,y):
    if x > 0 and y > 0:
        print('1')
    elif x > 0 and y < 0:
        print('4')
    elif x < 0 and y > 0:
        print('2')
    elif x < 0 and y < 0:
        print('3')
    else:
        print('0, 0')

chet(1, 1)
chet(-1, 1)
chet(1, -1)
chet(-1, -1)
chet(0, 0)
