#!/usr/bin/env python
# coding: utf-8

from random import randint

print("Welcome to the Geometry Game.")


# Create a Point class with coordinates x,y and method checking if coordinates are in the rectangle object
class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def falls_in_rectangle(self, rectangle):
        
        if rectangle.point1.x < self.x < rectangle.point2.x \
        and rectangle.point1.y < self.y < rectangle.point2.y:
            return True 
        else: 
            return False
        
# Create a Rectangle class to declare rectangle object and area method
class Rectangle:
    
    def __init__(self, point1, point2):
        
        self.point1 = point1
        self.point2 = point2
        
    def area(self):
        
        return (self.point2.x - self.point1.x) * (self.point2.y - self.point1.y)
 
# Create a random rectangle object
rectangle = Rectangle(
    Point(randint(0,9), randint(0,9)),
    Point(randint(10,19), randint(10,19)))

# Print generated rectangle points with their coordinates 
print("Rectangle cooridnates: ",
     rectangle.point1.x, ",",
     rectangle.point1.y, "and", 
     rectangle.point2.x, ",",
     rectangle.point2.y)

# Ask user for coordinates guess 
user_point = Point(float(input("Guess X: ")),
                   float(input("Guess Y: ")))

# Ask user for area guess 
user_area = float(input("Guess the rectangle area: "))

# Use falls_in_rectangle method to tell user whether the point is inside rectangle or not 
print("Your point was inside rectangle: ",
      user_point.falls_in_rectangle(rectangle))

# Use area method to calculate the guess
print("Your area is off by: ", 
      rectangle.area() - user_area)

