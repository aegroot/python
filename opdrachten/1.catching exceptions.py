def prijs():
    lst = ['een', 'twee', 'drie', 'vier', 'vijf', 'zes', 'zeven', 'acht', 'negen', 'tien', 'elf', 'twaalf', 'dertien',
           'veertien', 'vijftien']
    pers = eval(input("met hoeveel personen? \n in cijfers a.u.b"))
    pers2 = 0
    for i in lst:
        if pers in lst:
            pers2 = (int(lst.index(i)) + 1)
    if pers2 == 0:
        print("delen door 0 kan niet!")
    if pers2 < 0:
        print("Negatieve getallen zijn niet toegestaan!")
    kosten = (4356 / pers2)
    print(pers2)
    print(i)
    # print(kosten)


prijs()
