#enter a number and it will return all its positive divisors
a=int(input("Value : "))
b=0
c=1
while b!=a:
    b=b+1
    c=a%b
    if c==0:
        print(b)
