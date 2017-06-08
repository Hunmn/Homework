import random
a='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'
c = random.choice(a)

def rand_pass(n):
    return ''.join(random.choice(a) for i in range(n))

print(rand_pass(15))

