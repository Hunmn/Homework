import time
import random


def pause(n):
    def decorator(func):
        def wrapper(*args,**kwargs):
            print('Ждём {} сек...'.format(n))
            time.sleep(n)
            print('Прошло {} сек:'.format(n))
        return wrapper
    return decorator


a='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'
c = random.choice(a)


@pause(int(input('Зедержка: ')))
def password(n):
    yield ''.join(random.choice(a) for i in range(n))

gen = password(int(input('Количество символов: ')))
print('Пароль: {}'.format(next(gen)))


