#Lambda Fuction in python
# A lambda fuction in python is a small, anonymous funtion defined using the keywaord Lambda
#It can have any number of argument but only one expression, which evaulated and returned .

#Syntax :- lambda arguments: expression
#arguements : input to the funtion
#expression: A single statement or operation that lambda function retunred

add = lambda x, y : x+y
print(add(5,6))

#custom sorting - sort a list of tuples by thr second element

data = [(1,'b'),(3,'c'),(2,'a')]
print(data)
print(type(data))
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)
