def wijzig(list):
    del list[:]
    list.append("d")
    list.append("e")
    list.append("f")
    print(list)


lijst = ["a", "b", "c", "d", "e", "f"]
print(lijst)
wijzig(lijst)
