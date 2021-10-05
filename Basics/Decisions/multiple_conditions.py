# ask the user if it is sunny and breezy
print("is it sunny?")
is_sunny = input().lower()

print("is there a breeze")
is_breeze = input().lower()

if is_sunny == "yes" and is_breeze == "yes":
    print("clothes are dry")
else:
    print("clothes are not dry")