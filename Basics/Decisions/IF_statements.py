# ask user for the age
print("Please enter your age")

# read the user's response
age = int(input())

# decide if the person is an adult or child
if age >= 18:
    print("This user is an adult (over or equal to 18 years old)")

# use elif to check if they're below 18 but above 13
elif age >= 13:
    print("You are a teenager")

# final decision for the program to make
else:
    print("You are a child (under 18)")

print("End of program")
