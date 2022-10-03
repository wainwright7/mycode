#!/usr/bin/python3
""" Alta3 | Jay
    Pie Chart """

import matplotlib.pyplot as plt
import time

print("Welcome to the Pizza Factory..!!")
option = input("Want to order one? Please type- Yes or no : ")

if option.lower() == "yes":
    print("Add amount of following toppings in % you want on your pizza.")
    time.sleep(1)
    cheese = input("How much cheese you want?: ")
    time.sleep(1)
    onions = input("How much onions you want?: ")
    time.sleep(1)
    peppers = input("How much bell peppers you want?: ")
    time.sleep(1)
    mash = input("How much mashrooms you want?: ")
    time.sleep(1)
    spinach = input("How much spinach you want?: ")
    time.sleep(1)
    zuchini = input("How much zucchini you want?: ")
    time.sleep(1)
    print("This may take little time to get it perfect....", end=' ', flush=True)
    time.sleep(2)
    print("....", end= ' ' , flush=True)
    time.sleep(2)
    print("..", end= ' ' , flush=True)
    time.sleep(2)
    print(".", end= ' ' , flush=True)
    time.sleep(2)
    print("Ready! Your pizza has been served in the Static Directory!")

    labels = 'Cheese', 'Onions', 'Bell Peppers', 'Mashrooms', 'Spinach', 'Zuchini'  
    sizes = [int(f"{cheese}"), int(f"{onions}"), int(f"{peppers}"), int(f"{mash}"), int(f"{spinach}"), int(f"{zuchini}")]

    explode = (0.1, 0, 0, 0, 0, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    
    plt.savefig("/home/student/mycode/graph/veggiePizza.png")
    plt.savefig("/home/student/static/veggiePizza.png")
    plt.savefig("/home/student/static/veggiePizza.pdf")
else:
    print("Thank you for visiting, Come again :)")

