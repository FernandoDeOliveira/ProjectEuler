# menos linhas ~~~ antes de otimizar maior_fat_primo2
def is_primo(n):
    for i in range(2, n):
        if n % i == 0: return False
    else: return True
def maior_fat_primo1(n):
    for i in range(2, n):
        if is_primo(i):
            if n % i == 0: return maior_fat_primo1(n // i) if n % i == 0 else None
    else: return n


# mais rápido ~~~ internet
def maior_fat_primo2(x):
    A = []
    for y in range(2, x):
        if x == y:
            A.append(y)
            break
        while x % y == 0:
            x = x / y
            A.append(y)
    return A


# maior_fat_primo2 otimizado
def maior_fat_primo3(x):
    for y in range(2, x):
        if x == y: return y
        while x % y == 0:
            x = x / y


n = 600851475143
print(maior_fat_primo1(n), maior_fat_primo2(n)[-1], maior_fat_primo3(n))
