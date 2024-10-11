import math

def pizza_value(diameter, price):
    radius = diameter / 2
    area = math.pi * (radius ** 2)
    return area / price

diameter1 = float(input("What is the diameter of your first pizza? Enter the number only: "))
price1 = float(input("What is the price of your first pizza in dollars? Enter the number only: "))

diameter2 = float(input("What is the diameter of your second pizza? Enter the number only: "))
price2 = float(input("What is the price of your second pizza in dollars? Enter the number only: "))

value1 = pizza_value(diameter1, price1)
value2 = pizza_value(diameter2, price2)

average_value = (value1 + value2) / 2

if abs(value1 - value2) / average_value < 0.01:
    print("Within 1%, you get the same amount of pizza per dollar with either pizza. Yay!")
else:
    if value1 > value2:
        print("The first pizza gets you the most pizza per dollar.")
    else:
        print("The second pizza gets you the most pizza per dollar")