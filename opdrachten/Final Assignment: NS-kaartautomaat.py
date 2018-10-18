stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Aloterdijk', 'Amsterdam centraal',
            'Amsterdam Amstel', 'Utrecht Centraal', 's-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard',
            'Maastricht']


def inlezen_beginstation():
    station_begin = input("beginstation")
    while station_begin not in stations:
        print("we gaan niet naar " + str(station_begin))
        station_begin = input("beginstation")
    return station_begin


def inlezen_eindstation():
    station_eind = input("eindstation")
    while station_eind not in stations:
        print("we gaan niet naar" + str(station_eind))
        station_eind = input("eindstation")
    return station_eind


def omroepen_reis(station_eind, station_begin, stations):
    print("beginstation: " + str(station_begin) + "nummmer: " + str(stations.index(station_begin)))
    station_lengte = abs(stations.index(station_eind) - stations.index(station_begin))
    for getal in stations:
        if stations.index(getal) < stations.index(station_eind) and stations.index(getal) > stations.index(
                station_begin):
            print(getal)
    print("eindstation: " + station_eind + "nummmer: " + str(stations.index(station_eind)))
    print("de afstand beslaat " + str(station_lengte) + "stations")
    prijs = 5 * station_lengte
    print("de prijs is " + str(prijs) + "euro")


beginstation = (inlezen_beginstation())
print(beginstation)
eindstation = (inlezen_eindstation())
omroepen_reis(beginstation, eindstation, stations)
