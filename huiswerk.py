import math
print(math.pi)
ans = input("what is your name")
minus = (math.pi - len(ans))
if minus <= 0:
    print ("pi is shorter then the length of your name")
else:
    print ("pi is longer then the length of your name")
