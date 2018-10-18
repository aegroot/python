som = 0
nr = 0
getal = 1
while int(getal) > 0:
    getal = int(input("geef een getal: "))
    som = getal + som
    if getal == 0:
        break
    nr = 1 + nr

print("de som is: " + str(som))
print("er zijn " + str(nr) + " getallen ingevoerd")
