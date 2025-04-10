
from math import sqrt

a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

d = (b*b) -4 *(a *c)

if a == 0 or d <0:
    
    print("Impossivel calcular")

else:

    x2 = (-b - sqrt(d))/(2*a)
    x1 = (-b + sqrt(d))/(2*a)

    print(f"R1 = {x1:.5f}")
    print(f"R2 = {x2:.5f}")

# %%
