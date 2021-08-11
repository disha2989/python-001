import math

l=int(input('enter the length'))
b=int(input('enter the bredth'))
h=int(input('enter the height'))
print(l)
print(b)
print(h)

k= l**2 + b**2 + h**2

volume= (b**2 + h**2)/math.sqrt(k)

print(volume)
radius=((volume*3)/(4*3.14))** (1/3)
print(radius)
