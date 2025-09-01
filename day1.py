# Micro-task 01: Print today's date and my name

from datetime import datetime
name = str(input("Your name please..."))
print("Hello! Today's date ~")
print(datetime.today().strftime("%Y-%m-%d"))
print(f"My name is ~ {name}")
