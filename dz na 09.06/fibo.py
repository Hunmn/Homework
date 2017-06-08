def fibo(n):
    a = [1,1]
    for i in range(n-2):
        summ = a[-1] + a[-2]
        a.append(summ)
    return a

print(fibo(30))
