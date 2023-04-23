a = int(input("Введите число: "))
b = int(input("Введите степень: "))

def power(a, b):    
    if a == 1:
        return 1
    elif b == 1:
        return a
    else:
        return a*power(a, b-1)

print(power(a, b))
