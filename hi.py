First_Number = input("Please Input A Binary Number: ")
Second_Number = input("Please Input A Binary Number: ")
FNumberLen = len(First_Number)
SNumberLen = len(Second_Number)

BigNumber=[0]
SmallNumber=[0]
Sum=[]
Zero = 0
One = 1

if FNumberLen == SNumberLen:
    for i in range(FNumberLen):
        BigNumber.append(int(First_Number[i]))
    for i in range(SNumberLen):
        SmallNumber.append(int(Second_Number[i]))
if FNumberLen > SNumberLen:
    for i in range(FNumberLen - SNumberLen):
        SmallNumber.append(Zero)
    for i in range(FNumberLen):
        BigNumber.append(int(First_Number[i]))
    for i in range(SNumberLen):
        SmallNumber.append(int(Second_Number[i]))

l=0

if FNumberLen < SNumberLen:
    for i in range(SNumberLen - FNumberLen):
        SmallNumber.append(Zero)
    for i in range(SNumberLen):
        BigNumber.append(int(Second_Number[i]))
    for i in range(FNumberLen):
        SmallNumber.append(int(First_Number[i]))

print(BigNumber)
print(SmallNumber)
BigNumberLen = len(BigNumber) -1
SmallNumberLen= len(SmallNumber) -1

for i in range(BigNumberLen+1):
    z = BigNumber[BigNumberLen-i]
    x = SmallNumber[SmallNumberLen-i]
    if x == 0 and z == 0:
        Sum.append(Zero)
    if z == 1 and x == 0:
        Sum.append(One)
    if z == 0 and x == 1:
        Sum.append(One)
    if z == 1 and x ==1:
        Sum.append(Zero)
        l = SmallNumber[SmallNumberLen-i-1] = One
        l=  int(SmallNumber[SmallNumberLen-i-1])


Sum.reverse()
print(Sum)
y=len(Sum)
x=0
b=0
v=1

for i in range(1,y+1):
    z = Sum[y-i]
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
