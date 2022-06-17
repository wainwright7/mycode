#!/usr/bin/env python3

'''Tell me your credit score 
   600-850'''

#user gets total 5 tries
turn = 0

while turn < 5:

    #asks user to provide input 
    score = input("Provide your credit score between 600 to 850 : ")
    turn += 1

    #to make sure user's input is in numbers / digits
    if score.isdigit():
        score = int(score)
    else:
        print("That is not a valid number!")    #if input not in numbers
        continue
    #after all 5 tries loop breaks
    if turn == 5:
        print("Please try again!")
        break
   #if the score is greater than 850
    if score > 850:
        print("Too High!, Put number between 600 to 850")
        continue
    #if the score is less than 600
    if score < 600:
        print("Too low! Put number between 600 to 850")
        continue

    #output based on input provided
    if score < 700:
        print("Poor credit, Build your credit")
        break
    elif score >= 700 and score <=800:
        print("Good Credit!")
        break
    elif score >800:
        print("Excellent Credit!")
        break
