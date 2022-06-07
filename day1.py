#!/usr/bin/env python3
import random

wordbank = ["four" , "spaces" ]

tlgstudents= ["Aaron", "Casey", "Donny", "Emmanuel", "Eric", "Jaelen", "James", "Jay", "John", "Ken", "Maurice", "Mike", "Ryan", "Shamain", "Tuang", "Tyler", "Zhenqian", "Travis"]

num = input("Pick a number between 0 and 17: ")
num = int(num)

student_name = tlgstudents[num]
num1 = wordbank[0]
num2 = wordbank[1]

print(f"{student_name} always uses {num1} {num2} to indent.")




