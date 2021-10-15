print("Program Started!")
code = int(input("Please enter an ASCII code (between 32 - 126): "))


def findChar(code):
    character = chr(code)
    if code in range(33, 126):
        print(f"ASCII code {code} = Character {character}.")
    elif code == 32:
        print(f"ASCII code {code} = Space(\" \").")


while code not in range(32, 126):
    code = int(input("Please enter an ASCII code (between 32 - 126): "))

else:
    findChar(code)