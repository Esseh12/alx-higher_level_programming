#!/usr/bin/python3
x = int(input('Enter a number: '))
if x < 0:
    x = 0
    print('Number has been changed to zero')
elif x == 0:
    print('Number entered is zero')
elif x == 1:
    print('Number entered is one')
else:
    print('You have entered a large number')
