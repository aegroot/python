infile = open("kaartnummers.txt", "r")
regels = infile.readlines()
infile.close()
lst = []
for regel in regels:
    kaartinfo = regel.split(",")
    kaartinfo[1].strip()
    lst.append(kaartinfo)
ind_max = (lst.index(max(lst))) + 1
print('deze file telt ' + str(len(lst)) + " regels")
print("het grootste kaartnummer is: {} en dat staat op regel {}".format(max(lst)[0], str(ind_max)))
