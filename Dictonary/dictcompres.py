# Dictionary Comprehension
#A dictiornary comprehension allows you to create dictionaries in a concise way.

#syntax :- New_dict {key_expression: value_expression for item in iterable if condition}
#example: creating a dictionary with square number 

New_dict = {
    x:x*x for x in range(1,10)
}

print(New_dict)

