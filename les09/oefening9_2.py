week = {'ma': 'maandag', 'di': 'dinsdag', "wo": 'woensdag', 'do': 'donderdag', 'vr': 'vrijdag'}
print(week['ma'])
print(len(week))
week['za'] = 'zaterdag'
print(week)
for afkorting in week.keys():
    print(afkorting)
for naam in week.values():
    print(naam)
for afkorting in week.keys():
    print(afkorting, week[afkorting])
