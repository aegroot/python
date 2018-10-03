paspoort = (input("heb jij een paspoort?"))
leeftijd = int(input("wat is jou leeftijd?"))
if leeftijd > 18 and paspoort == "waar":
    print("nederlands paspoort: ja")
    print("Gefeliciteerd, je mag stemmen!")
else:
    print("je bent niet geslaagd of je hebt geen paspoort!")
