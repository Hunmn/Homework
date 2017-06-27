import time
import random
from time import sleep

a='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'
c = random.choice(a)

def password(n):
    yield ''.join(random.choice(a) for i in range(n))

gen = password(int(input('Количество символов: ')))

print(next(gen))



def pause(n):
    def decorator(func):
        def wrapper(*args,**kwargs):
            print('Ждём {} сек...'.format(n))
            time.sleep(n)
            print('Прошло {} сек:'.format(n))
        return wrapper
    return decorator


@pause(3)
def password_sleep(n):
    return ''.join(random.choice(a) for i in range(n))

print(password_sleep(10))

