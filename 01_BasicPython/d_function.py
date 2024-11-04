import math 

#1. def funName(____):
def sqr(num):
    return num**2

# function polymorphism

def mul(p1, p2):
    return p1*p2

# print('a',3)
# print(3*4)
# print(5, 'q')


# function returning multiple values

def circle_stats(radius):
    perimeter = 2*math.pi*radius
    area = math.pi*radius*radius

    return perimeter, area

cirArea, cirPerimeter = circle_stats(3)
# print("circumference is " , format(cirPerimeter, "0.3f") , "area is " , format(cirArea, "0.6f"))



# default parameter value

def greet(name = "User"):
    return "Hello " + name

print(greet("aman"))
print(greet())

