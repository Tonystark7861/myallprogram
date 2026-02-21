#add modify

Superhero = {
        'Name'   : 'Krish',
        'Powers' :  'Superhuman Strensth',
        'age'     :  36,
        'City'    :  'Mumbai',
        'Enemy'   :  'Kaal'
}

for key, value in Superhero.items():
    print(key, ":", value)

print(Superhero.keys())
print(Superhero.values())
print(Superhero.items())

# add item or remove item in dictionary

Superhero['weapon'] = 'nanchaku'

print(Superhero)

Superhero['age'] = '33'
print(Superhero)

del Superhero['weapon']
print(Superhero)

# .pop method is important 

vat1 = Superhero.pop('City')
print(vat1)
print(Superhero)



