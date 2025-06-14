import math

def circleState(radius):
    area = math.pi * radius ** 2;
    circumference = 2 * math.pi * radius
    return area,circumference

a,c = circleState(5)

print(f"Area : {a} \nCircumference : {c}")