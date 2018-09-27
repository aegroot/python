def new_password() -> object:
    newpassword = str(input("type your password"))
    if newpassword is not oldpassword and len(newpassword) > 5:
        print("true")
    else:
        print("false")
    return new_password()


oldpassword = "functie"
new_password()
