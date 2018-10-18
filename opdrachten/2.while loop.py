ans = ""
while len(ans) != 4:
    if len(ans) == 4:
        break
    ans = input("Geef een string van vier letters: ")
    print("{}heeft {} letters: goed zo!".format(ans, len(ans)))
    continue
