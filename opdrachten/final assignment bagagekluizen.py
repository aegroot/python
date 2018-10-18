def toon_aantal_kluizen_vrij():
    infile = open("kluizen.txt", "r")
    regels = (infile.readlines())
    list = []
    for getal in regels:
        list.append(getal.split(","))
    print(list)
    infile.close()
    som = 0
    for getal in list:
        if getal[1] == 'false\n' or getal[1] == 'false':
            som = som + 1
        else:
            continue
    print(som)


def nieuwe_kluis():
    nieuw = input("wachwoord voor nieuw account")
    keuze = input("wil je de kluis alvast bezetten?\ntrue of false")
    code = (input("voor een nummer tussen 1 en 12 in"))
    infile = open("kluizen.txt", "r")
    regels = (infile.readlines())
    list = []
    for regel in regels:
        list.append(regel.split(",")[0])
    infile.close()
    code1 = int(code)
    lijst = (list[code1]).replace(str(code1), nieuw, keuze)
    print(lijst)


def kluis_openen():
    kluisnummer = input("wat is je nummer")
    kluiscode = input("wat is je code")
    infile = open("kluizen.txt", "r")
    regels = infile.readlines()
    infile.close()
    for regel in regels:
        kluisinfo = regel.split(',')
        nummer = kluisinfo[0]
        code = kluisinfo[1].strip()
        gegevenscorrect = ()
        if (kluisnummer == nummer) and (kluiscode == code):
            gegevenscorrect = True
            if gegevenscorrect:
                print('De kluis is open! ')
        if (kluisnummer != nummer) and (kluiscode != code):
            continue
        if gegevenscorrect is False:
            print('Uw wachtwoord of kluisnummer is niet correct:')


# def kluis_teruggeven():
# in list[getal]:lst.replace(true,false)

ans = input(
    "1: Ik wil weten hoeveel kluizen nog vrij zijn \n2: Ik wil een nieuwe kluis \n3: Ik wil even iets uit mijn kluis halen \n4: Ik geef mijn kluis terug\ngeef een nummber a.u.b")

if ans == "1":
    toon_aantal_kluizen_vrij()
if ans == "2":
    nieuwe_kluis()
if ans == "3":
    kluis_openen()
