def kwadraten_som(lst) -> object:
    getal = 0
    for getal in lst:
        if getal > 0:
            getal = getal ** 2
            print(getal)


lst = [4, 5, 3, -81]
kwadraten_som(lst)
