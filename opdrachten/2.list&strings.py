# getal
#  = 0
vierplus = []
lst = eval(input("Geef lijst met minimaal 10 strings: "))
for getal in lst:
    if len(getal) == 4:
        vierplus.append((getal))
print("De nieuw-gemaakte lijst met alle vier-letter strings is:," + str(vierplus))
