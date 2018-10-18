try:
    numlist = [100, 101, 0, '103', 104]
    index = int(input("geef een index"))
    print(100 / numlist[index])
except ValueError:
    print("je moet een heel getal invoeren")
except ZeroDivisionError:
    print("de lijst bevat een 0")
except TypeError:
    print("de lijst bevat een string")
except IndexError:
    print("je moet een getal tussen 5 en -4 invoeren")
