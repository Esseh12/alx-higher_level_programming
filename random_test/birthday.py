#!/usr/bin/python3
# ask user for birthday and tore in a variable birthday
birthday = input('Enter your birthday: ')
birthday = int(birthday)
# use conditional statement to tell which is more important and which is less important
if birthday == 1 and birthday <= 18:
    print('Birthday is important')
elif birthday == 21 or birthday == 50:
    print('Birthday is important')
elif birthday <= 65:
    print('Birthday is important')
else:
    print('Birthday is not so important')
