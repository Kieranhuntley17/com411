
# name of person
name = input("what is your name?")
# age of person
age = int(input("what is your age? (years)"))
# weight of person
weight = int(input("what is your weight? (KG)"))
# height of person
height = float(input("what is your height? (meters)"))
# displays inputted name and the BMI is calculated by weight divided by height squared
print(f"your name is {name} and your bmi is {weight/height**2}")
