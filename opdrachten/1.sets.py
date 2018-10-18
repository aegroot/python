bruin = ["Boxtel", "Best", "Eindhoven", "Helmond `t hout", "Helmond", "Helmondbrouwhuis", "Deurne"]
groen = ["Boxtel", "Best", "Eindhoven", "geldrop", "heeze", "weert"]
print(bruin)
print(groen)
print("hebben beide met elkaar gemeen:")
for getal in bruin:
    for nummer in groen:
        if getal == nummer:
            print(getal)
print("hebben beide niet met elkaar gemeen:")
for getal in bruin:
    if getal not in groen:
        print(getal)
