s = "Guido van Rossum heeft programmeertaal Python bedacht."
s.split(" ")
print(s)
for getal in range(len(s)):
    if "a" == s[getal] or "e" == s[getal] or "i" == s[getal] or "i" == s[getal] or "u" == s[getal]:
        print(s[getal])
