lente = (3, 4, 5)
zomer = (6, 7, 8)
herfst = (9, 10, 11)
winter = (12, 1, 2)


def seizoen(a):
    maand = "sorry"
    if a in lente:
        maand = "lente"
    elif a in zomer:
        maand = "zomer"
    elif a in herfst:
        maand = "herfst"
    elif a in winter:
        maand = "winter"
    print(maand)


seizoen(7)
