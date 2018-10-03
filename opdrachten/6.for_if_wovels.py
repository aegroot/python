s = "Guido van Rossum heeft programmeertaal Python bedacht."
s.split(" ")
print(s)
for getal in range(len(s)):
    if "a" == getal or "e" == getal or "i" == getal or "i" == getal or "u" == getal:
        print(s[getal])
