#insérez un nombre, il vous renverra tout les diviseurs de ce dernier
a=int(input("Value : "))
b=0
c=1
while b!=a:
    b=b+1
    c=a%b
    if c==0:
        print(b)
