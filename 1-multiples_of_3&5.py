# SUM OF ALL NUMBERS THAT ARE MULTIPLES OF 3 OR 5 BELOW 1000
print(sum(i for i in range(1001) if i % 3 == 0 or i % 5 == 0))
