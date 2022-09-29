#!/usr/bin/python3
import random

"""Alta3 | Jay
   Working with list"""

def main():

    # creating a list of wordbank 
    wordbank= ["indentation", "spaces"]

    # creating a list of students names 
    tlgstudents= ["Aaron", "Andy", "Asif", "Brent", 
                  "Cedric", "Chris", "Cory", "Ebrima", 
                  "Franco", "Greg", "Hoon", "Joey", 
                  "Jordan", "JC", "LB", "Mabel", 
                  "Shon", "Pat", "Zach"]

    # appending a int to a wordbank list
    wordbank.append(4)
    
    num=int(input("Type a number between 0 and 18 : "))

    student_name = tlgstudents[num]

    print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.")

    superB = random.choice(tlgstudents)
    print(f"{superB} always uses {wordbank[2]} {wordbank[1]} to indent.")


main()
