import os

# path = os.getcwd()
# print(f"Current working directory: {path}")

# for file in os.listdir(path):
    # print(file)


def cwd():
    path = os.getcwd()
    print(f"Current working directory: {path}")
    for file in os.listdir(path):
        print(f"The directory contains the following files: {file}")

def run():
    print("Processing...")
    cwd()

run()