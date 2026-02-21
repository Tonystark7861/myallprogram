
# This Tutorial helps studnets and IT professionals to learn about python Set, 
#we have explained here its working and application using &,-,| opeartors.


#Here we have created 2 differnet Set.

setA = {12,23,34,45,56,56,67,78,78,89,90,67,90}
print(" this is first Set", setA)

setB = {11,22,23,34,44,55,66,7,78,90,87,}
print("this is second Set ", setB)

#union set method

setuni = setA.union(setB)
print("it will give unique number of both set",setuni)
print(type(setuni))
setunisign = setA | setB
print("this is using | sign", setunisign)


#Difference set method

setdifference  = setA.difference(setB)
print("Set difference items exist in Set A that do not exist in Set B \n", setdifference)
print(type(setdifference))
setdiffsign = setA - setB
print("this is using '-'  sign\n", setdiffsign)


#Intersection Set Method 

setintersection = setA.intersection(setB)
print("it will give common number of both set\n",setintersection)
print(type(setintersection))
setintersign = setA & setB
print("this is using & sign\n", setintersection)


# Set symmatric difference

setsymmaticdi = setA.symmetric_difference(setB)
print("it will give common number of both set\n",setsymmaticdi)
print(type(setsymmaticdi))
setsymmaticdisign = setA ^ setB
print("this is using & sign\n", setsymmaticdisign)


