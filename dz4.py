def  palindrom(word):
    a = str(word)
    if  a == a[::-1]:
        return True
    else:
        return False

print(palindrom('12321'))
print(palindrom('anna'))
