#!/usr/bin/python3
name = input("Enter your name: ")
while name == "":
    print("Name required")
    print("Enter your name: ")
else:
    print(f"hello {name}")

