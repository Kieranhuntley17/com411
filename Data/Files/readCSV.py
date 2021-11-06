import csv

def read(path):
    with open(path) as file:
        headings = file.readline().strip()
    print(f"Headings:\n{headings}")

    with open(path) as file:
        for line in file:
            line.strip()
            print(line)

read("bots.csv")