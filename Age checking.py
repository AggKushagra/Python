"""This program will tell if a person is an adult or not"""
age=int(input("Pls tell the age of the person:"))
if age<18:
    print("The Person is not an adult")
elif age>=18:
    print("The Person is an adult")
else:
    print("Error")
