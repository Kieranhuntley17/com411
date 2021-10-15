print("Program Started")
val = str(input("Please enter a character: "))

# runs a while loop to say while the length doesn't = 1 then ask for another input
while len(val) != 1:
    print("Enter valid Char")
    val = str(input("Please enter a character: "))


# creates a function to check what value the input has
def checkval(letter):
    value = ord(letter)

    if len(letter) == 1:
        print(f"letter {letter} = ASCII value {value}")


checkval(val)