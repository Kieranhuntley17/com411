import matplotlib.pyplot as plt


def coordinate():
    x = input("enter an x value")
    y = input("enter a y value")
    return (x, y)



def path():
    print("retrieving path...")
    x_values = []
    y_values = []
    for i in range(0, 4):
        coordinate()

