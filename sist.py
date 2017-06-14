def sist(n,x):
    if x == 16:
        d = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9',
         10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
        q = n
        result = ""
        while q != 0:
            r = q % 16
            q = q // 16
            result += d[r]
        result = ''.join(reversed(result))
        return result

    result = ""
    while n > 0:
        y = str(n % x)
        result = y + result
        n = int(n / x)
    return result


print(sist(123334,16))
print(sist(123334,2))
print(sist(123334,8))
