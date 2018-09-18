cijferICOR = 7
cijferPROG = 7
cijferCSN = 7
cijferGEM = ( cijferICOR + cijferPROG + cijferCSN ) / 3
cijferTOT = sum([cijferCSN ,cijferICOR ,cijferPROG])
beloning = (cijferTOT * 30)
print("mijn cijfers (gemiddeld " + str(cijferGEM) + ') leveren een beloning van ' + str(beloning) +" op")