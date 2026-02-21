# Dictionary Iteration :- Dictionary can be iterated using For loop.
# we can loop through dictionaries by using values  keys and both.

#create a dictionary 

MarvelComic = {
            'ChacName' : 'RealName',
            'Chcage'   : 'Realage',
            'Sklls'    : 'Powers',
            'Mainfoe'  : 'Enemy',
            'contact'  :  'phonenum',
            'email'    :  'marvel@gmil.com'
}

print(type(MarvelComic))
print(MarvelComic)

#Loop Through Keys

print("It will print only key iterate using for loop\n")

for key in MarvelComic:
    print(key)

#Loop through values


print("It will print only value iterate using for loop\n")

for value in MarvelComic:
    print(value)

#loop through both values and keys

print("It will print both keyand value pair iterate using for loop\n")

for key, value in MarvelComic.items():
          print(key,value)

    