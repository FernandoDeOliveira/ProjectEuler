def smallestMultiple(*args):
    numbers = [i for i in args]
    if numbers:
        n = max(numbers)
        m = n
        numbers.remove(n)
        while any(n % number for number in numbers):
            n += m
        return n
    return 0

numbers = [i for i in range(1,11)]
print(smallestMultiple(*numbers))