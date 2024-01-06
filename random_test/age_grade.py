#!/usr/bin/python3
# Ask user to input age and use eval to change the string to an integer while saving it in a variable called age
age = eval(input('What is your age: '))
# use conditional statement for age 1 - 5 to go to kindergarteen
if (age >=  1) and (age <= 5):
    print('Go to kindergateen')
# use conditional statement for age 6 - 17 to grade 1 - 12
elif (age == 6) and (age <= 17):
    grade = age - 5
    print(f" you should be in grade {grade}")
else:
    print('You should be in college')

