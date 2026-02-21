# Nested Dictionary 
#Dictionary can contain other dictinaires, which is useful for storing more complex data.

#nested dictionaries

main_student = {
       
         'student1' : {'name': 'Madhav', 'age': 30,'city': 'indore'},
         'student2' : {'name': 'Keshav', 'age': 31,'city': 'bhopal','grade': 'A'}
}

print(main_student)

#if we want to print a single dictionary 

print(main_student['student1'])

#if we want to access single value from nested dictionary

print(main_student['student1']['name']) 

