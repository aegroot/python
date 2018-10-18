zin = ("all animals are equal but some are more equal than others")
lst = zin.split(' ')
woordenteller = {}
for woord in zin:
    if woord in woordenteller:
        woordenteller[woord] = +1
    else:
        woordenteller[woord] = 1
for woord in woordenteller:
    print('{:8} komt {} keer voor'.format(woord, woordenteller[woord]))
