def gemmiddelde():
    zin = str(input("voer een willekeurige zin in"))
    zin_gem = len((zin.replace(" ", ""))) / len(zin.split(" "))
    print(zin_gem)


gemmiddelde()
