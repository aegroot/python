def standaardprijs(afstandkm):
    if afstandkm < 0:
        prijs1 = 0
    elif afstandkm > 0 and afstandkm < 50:
        prijs1 = (afstandkm * 0.8)
    elif afstandkm > 50:
        prijs1 = (15 + afstandkm * 0.6)
    return prijs1


def ritprijs(leeftijd, weekendrit):
    prijs = standaardprijs(afstandkm)
    if leeftijd < 12 or leeftijd > 65:
        prijs = 0.7 * prijs
    elif weekendrit == True and leeftijd < 12 or leeftijd > 65:
        prijs = 0.65 * prijs
    elif weekendrit == True and leeftijd > 12 and leeftijd < 65:
        prijs = prijs * 0.6
    print(prijs)
    return prijs


leeftijd = int(input("leeftijd?"))
weekendrit = eval(input("weekendrit?"))
afstandkm = int(input("wat is uw afstand?"))
kosten = ritprijs(leeftijd, weekendrit)
# print (kosten)
# print (ritprijs(leeftijd,weekendrit))
