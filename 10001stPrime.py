def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True


def nth_prime(n):
    prime = 1
    while n != 0:
        prime += 1
        if is_prime(prime):
            n -= 1
    return prime

print(nth_prime(10001))