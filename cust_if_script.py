#!/usr/bin/python3

message = 'Your score converted in to grade is : '

grade = float(input("How much did you score in your last test out of 100 points? : "))

if grade <=100 and grade >= 90:
    message = message + 'A Grade'

elif grade <= 89 and grade >= 80:
    message = message + 'B Grade'

elif grade <=79 and grade >=  70:
    message = message + 'C Grade'

elif grade <= 69 and grade >= 60:
    message = message + 'D Grade'

elif grade <= 59:
    message = message + 'F Grade'

else:
    message ='Please provide correct score between 0 to 100.'

print(message)

