# Micro-task 02: Age Calculator

# TBD:
# - Calculate current age (in years)
# - Print whether they are an adult (18+) or a minor (<18)
# - Must handle edge cases (e.g., if the birth year is in the future)
# - Extend the program so it also tells the user in which year they will turn 100 years old

# Input: Birth year = 2000  
# Output: You are 25 years old. You are an adult.  
#         You will turn 100 in the year 2100.  

from datetime import datetime

birth_year = int(input("Birth year: "))
current_year = datetime.now().year
age = current_year - birth_year

if age<0:
    print("Invalid birth year...")
else:
    status = "an adult" if age>=18 else "a minor"
    print(f"You are {age} years old. You are {status}!!")
    print(f"You will turn 100 in the year {birth_year+100}.")
