#!/usr/bin/python3
# Problem: write a program that coverts miles to kilometer
# Ask user to input a number in miles and save the input into a variable called miles
miles = input("Enter a distance in miles: ")
# Change the information saved into a integer
miles = int(miles)
# convert the number in miless to kilometer and stote the value in a variable called kilo
kilo = miles * 1.60934
# print the value in kilo to the user
print(f"{miles} miles = {kilo} kilometers")
