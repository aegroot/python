outfile = open("kaartnummersuit2.txt", "w")


def strftime():
    import datetime
    vandaag = datetime.datetime.today()
    s = vandaag.strftime(" %a %d %b %Y, %R:%S")
    return (s)


ans = input("voeg een aantal namen toe")

outfile.write("{} {}\n".format(strftime(), ans))
outfile.close()
