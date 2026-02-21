#set methodss
#Union combine elments from 2 sets and as result only gives unique value 
#we can use pipe symbol "|" instead keyword union to perform this
#Difference :- elements present in first set only but in 2nd 
#symmetric Set :- Elements in either set but not in both sets

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8,}

#union
union_set = set1.union(set2)
print(union_set)
print("Here we go interestin")

#intersection
intersection_set = set1.intersection(set2)
print(intersection_set)
print(type(intersection_set))

#Difference
difference_set = set1.difference(set2)
print(difference_set)

#symmetic set
symmetric_set = set1.symmetric_difference(set2)
print(symmetric_set)




#set Alternative 
#for union pls use "|",  Fir intersection pls use "&", For difference pls "-"

set3 = {'rola','khola','tola','A','B'}
set4 = {'tola','A','B','C','D','E'}
intersection_set2 = set3 & set4
union_set3 = set3 | set4
print(union_set3)
print("here we go intersection")
print(intersection_set2)
difference_set2 = set3 - set4
print("here we go difference")
print(difference_set2)