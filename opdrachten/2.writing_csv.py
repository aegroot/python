import csv

with open("newfile.csv", 'w', newline='')as myCSvFile:
    writer = csv.writer(myCSvFile, delimiter=';')
    # writer.writerow(('number','name'))
    number = 0
    while True:
        naam = input("Wat is je achternaam? ")
        number = number + 1
        if naam == '' or naam == "eind":
            break
        voorl = input("Wat zijn je voorletters? ")

        gbdatum = input("Wat is je geboortedatum? ")
        email = input("Wat is je e-mail adres? ")
        # number = input("nummer?")

        writer.writerow((number, naam, email, gbdatum, voorl))

# gebruik hier een herhalingslus:
# wanneer de volgende persoon inlogt is onbekend, dus schrijf meteen naar file
