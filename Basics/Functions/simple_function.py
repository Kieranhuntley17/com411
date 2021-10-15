def listen():
    sound = str(input("what sound did I hear(rumble)? "))

    while sound != str("rumble"):
        sound = str(input("what sound did I hear(rumble)? "))

    else:
        print(f"That was a loud {sound}")

listen()
