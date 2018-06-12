def largest_pali(n_digitos):
    for i in range(((10 ** n_digitos) - 1), 0, -1):
        for j in range(((10 ** n_digitos) - 1), 0, -1):
            if str(i * j) == str(i * j)[::-1]: return i*j
print(largest_pali(3))
