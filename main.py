#1-misol
import math

son = float(input("Musbat son kiriting: "))

ildiz = math.sqrt(son)

print("Kiritilgan sonning kvadrat ildizi:", ildiz)

#2-misol
import math

a = float(input("a ni kiriting: "))
b = float(input("b ni kiriting: "))

natija = math.sqrt(a**2 + b**2)
# yoki:
# natija = math.sqrt(math.pow(a, 2) + math.pow(b, 2))

print("Natija:", natija)

3-misol
import math

gradus = float(input("Burchakni gradusda kiriting: "))

radian = math.radians(gradus)
sinus = math.sin(radian)

print("Burchakning sinusi:", sinus)
