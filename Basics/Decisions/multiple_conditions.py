# ask the user if it is sunny and breezy
print("is it sunny?")
is_sunny = input().lower()

print("is there a breeze")
is_breeze = input().lower()

# or can be used instead of and. this means only one of the conditions need to be true
if is_sunny == "yes" and is_breeze == "yes":
    print("clothes are dry")
else:
    print("clothes are not dry")