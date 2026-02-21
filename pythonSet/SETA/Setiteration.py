#Set Iteration 
#set comprehension
#Set iteration can be achieved by using for loop but it is not possible to use while loop directly 
#for this we need to convert set into list than we will be using while to iterate set
#The main reason behind it is while loop uses index and set is not oredered therfore while loop cannot be used.


#set iteration using For loop

numbers = {1,2,3,4,5,67}
for i in numbers:
    print(i)