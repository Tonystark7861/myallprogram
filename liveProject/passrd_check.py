#password strength checker

import re

# password strength check conditions :
# min 8 chars, digit atleast one, uppercase, lowercase, special charatcer

def check_password_strength(password):
      if len(password) < 8: # length of password
            return "Weak: password must be at least 8 chars"
      
      if not any(char.isdigit() for char in password):
            return "Weak: Password must contain a digit"
      
      if not any(char.isupper() for char in password):
            return "Weak: password must contain atleast one upper charecter"
      
      if not any(char.islower() for char in password):
            return "Weak: password must contain atleast one lower charecter"
      
      if not re.search(r'[!@#$%^&*(){}<>.?]', password):
            return "Medium: password must contain a special character" 


      return " Strong:  Your password is Secure" 


def password_checker():
      print("we are checing passowrd here")

      while True:
            password = input("Enter you password ( or type 'exit' to quit): ")

            if password.lower() == 'exit':
               print("Thank you for using this tool")
               break
            Result = check_password_strength(password)
            print(Result)

# Run the password checker tool

if __name__  == "__main__":
      password_checker()