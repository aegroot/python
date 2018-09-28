def lang_genoeg() -> object:
    length = int(input("wat is uw lengte?(in cm)"))
    if length > 119:
        print("je bent lang genoeg voor de attractie!")
    else:
        print("Sorry, je bent te klein")
    return lang_genoeg()
lang_genoeg()
