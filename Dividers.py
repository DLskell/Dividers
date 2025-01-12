#enter a number and it will return all its positive divisors
a=int(input("Value : "))
for b in range(2, a):
    c = a % b
    if c == 0: print(b)
