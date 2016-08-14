fibonacci=[]
x=0
y=1
num = int(input("Lista Fibonacci menor que:"))
fin = False
while (not fin):
    if (x + y >= num):
        fin = True
    else:
        fibonacci.append(x+y)
        aux = x + y
        x = y
        y = aux
print(fibonacci)