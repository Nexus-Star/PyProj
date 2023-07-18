print("Hello, This Program is Capable Of Converting Any Binary Number To A Decimal Number")
Number = input("Please Input A Binary Number: ")
y= len(Number)
b=0
v=1
x=0
Number = Number.replace(""," ")
Number = Number.split()
for i in range(y):
    Number[i]=int(Number[i])
for i in range(1,y+1):
    z = Number[y-i]
    if b >=2:
        z=z*v
        v=v*2
        x=x+z
    if b == 1:
        z=z*v
        v=v*2
        b = 2
        x=x+z
    if b==0:
        z=z*v
        v=v*2
        b = 1
        x = x+z
print(x)