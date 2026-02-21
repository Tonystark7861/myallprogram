#dictionary :- Basically Dictionary  stores data in key : value pairs.
#Key must Always be Unique and immutable 
#One of the Best way of creating  dictionary is passing KEy : value pair as Tuple 

#IN this Example we simply pass tuples key value pair in dictinary as argument

#let's see example of adding details of a person biodata
#This is idustrial and most common method of creating dictionary in python

persondetails = dict([
                      ('Name','Abhishek'),
                      ('Age',32),
                      ('Job','ITSO'),
                      ('Feild','Banking'),
                      ('City','Mumbai')
])

print(persondetails)
print(type(persondetails))

#Here we can see these input tuples are now convert as dictionary Key Value Pair
#Accessing Dictionary :- BEst way is to For loop for calling dictionary 

print(persondetails.keys())
print(persondetails.values())
print(persondetails.items())

for key, value in persondetails.items():
    print(key, ":", value)
