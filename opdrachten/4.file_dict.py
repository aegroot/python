def ticker():
    ans = input("Enter Company name: ")
    infile = open("file_dict.txt", "r")
    company = infile.readlines()
    infile.close()
    regeltjes = []
    for i in company:
        regeltjes.append(i.split(":"))
    regels = {}
    for i in regeltjes:
        regels[i[0]] = i[-1]
    for regel in regels:
        if regel == ans:
            print(regels[ans])
        else:
            continue


def company():
    ans = input("Enter Ticker symbol: ")
    infile = open("file_dict.txt", "r")
    company = infile.readlines()
    infile.close()
    regeltjes = []
    for i in company:
        regeltjes.append(i.split(":"))
    regels = {}
    for i in regeltjes:
        regels[i[0]] = i[-1]
    inv_map = {v: k for k, v in regels.items()}
    for regel in regels:
        if regel == ans:
            print(inv_map[ans])
        else:
            continue


ticker()
