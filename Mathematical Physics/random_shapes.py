import random
import math

def square_area():
    side = random.randint(1,100)

    return side**2

def triangle_area():
    base = random.randint(1,100)
    height = random.randint(1,100)

    return 1/2 * base * height

def rectangle_area():
    length = random.randint(1,100)
    width = random.randint(1,100)

    return length * width

def circle_area():
    radius = random.randint(1,100)

    return math.pi * radius **2 

def parallelogram_area():
    base = random.randint(1,100)
    height = random.randint(1,100)

    return base * height

print(square_area())
print(rectangle_area())
print(triangle_area())
print(circle_area())
print(parallelogram_area())

