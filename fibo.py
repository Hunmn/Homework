


def fibo(n):
    x = 0
    k = 1
    yield k
    for i in range(n-3):
        x += k
        yield x
        if i <= n:
            k += x
            yield k

lst = (str(i) for i in fibo(int(input(''))))
print(' '.join(list(lst)))
