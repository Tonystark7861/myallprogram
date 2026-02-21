# Find Intersection (common element of Two List)

list1 = [1,2,3,4,5,6,7,8,]
list2 = [3,5,6,7,9,18,45,]

#first we use for loop to find common 

# In this we just eed to define function and using for loop

def intsec_loop(lag1, lag2):
    common_list = []
    for item in lag1:
        if item in lag2 and item not in common_list:
            common_list.append(item)
    return common_list

print(intsec_loop(list1, list2))

#Now make the same thing using List Comprehension
# List Compresin simply one line syntax use for loop and cpmpact all thing in square brcket as we need list 

def intersection_comp(lst1,lst2):
    return [item for item in lst1 if item in lst2]

print(intersection_comp(list1,list2))





