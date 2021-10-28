import os

def display_chars(path, chars):
    with open(path) as file:
        partial_data = file.read(chars)
        return partial_data

print(f"the first 5 chars of library.txt are \"{display_chars('library.txt', 5)}\"")

def display_line(path):
    with open(path) as file:
        line = file.readline().strip()
        return line

print(f"The first line of library.txt is \"{display_line('library.txt')}\"")

def display_text(path):
    with open(path) as file:
        data = file.read()
        lines = data.split("\n")
        return lines

print(f"The first line of library.txt is \"{display_text('library.txt')}\"")