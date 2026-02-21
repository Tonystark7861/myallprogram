# oops in python
#oop- Object oriented progrmming

# student_1 = ['madhav', 10]
# student_2 = ['vipul', 12]
# student_3 = ['neem', 56]


# print(f'{student_1[0]} is in class {student_1[1]}')
# print(type(student_1))

#using OOPs - creating student records
#self parameter - reference or connection build between object
#class - blueprint or template 

class Student:  #student class
    def __init__(self,full_name, class_grade, percentage):  #init method is constructor used to initialize method
        self.name = full_name            # self paramter is used toi build connection object and class and help to pass paramter 
        self.grade = class_grade
        self.percentage = percentage

    def student_details(self):
        print(f"{self.name} is in class {self.grade}, with {self.percentage}%")

#object - instnace
student_1 = Student('Tonystark', 44,56)
#print(student_1.name, student_1.grade)

student_2 = Student('ironman', 67,78)
#print(student_2.name, student_2.grade)

student_1.student_details()
student_2.student_details()

print(student_1.__dict__)   # Gives output in form of dictiornay
print(student_2.__dict__)

print(type(student_1.__dict__))  
print(type(student_2.__dict__))

#modifey the property of object 

print(student_1.percentage)
student_1.percentage = 100
print(student_1.percentage)

#Delete 
del student_1
print(student_1)


