def code():
    list = []
    txt = input("voer je naam in")
    print(txt)
    txt = (([ord(c) for c in txt]))
    print(txt)
    for i in txt:
        list.append(chr(i + 3))

    print(list)


code()
