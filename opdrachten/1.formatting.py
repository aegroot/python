def convert(i):
    F = (i * 1.8 + 32)

    if F < 0 and i < 0 and len(str(i)) != 2 and len(str(F)) == 4:
        print("{}   {}".format(float(i), F))
    elif F < 0 and i < 0 and len(str(i)) != 2 and len(str(F)) != 4:
        print("{}  {}".format(float(i), F))
    elif F < 0 and i > 0 and len(str(i)) == 3:
        print(" {}   {}".format(float(i), F))
    elif F > 0 and i > 0 and len(str(F)) == 5:
        print(" {}  {}".format(float(i), F))
    elif F > 0 and i > 0 and len(str(F)) == 4:
        print(" {}   {}".format(float(i), F))


def table():
    print("  C   F")
    for i in range(-30, 41, 10):
        convert(i)


table()
