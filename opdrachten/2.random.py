import random

lst = 0
'''def monopoly():
    rol1=int(random.randint(1, 6))
    rol2=int(random.randint(1, 6))
    ans=rol1+rol2
    print(str(rol1) + "+" + str(rol2) + " = " + str(ans))'''

while lst < 3:
    rol1 = int(random.randint(1, 6))
    rol2 = int(random.randint(1, 6))
    ans = rol1 + rol2
    print(str(rol1) + "+" + str(rol2) + " = " + str(ans))
    if rol1 == rol2:
        lst = lst + 1
    if rol1 != rol2:
        break
if lst == 3:
    print("naar de gevangenis!")
