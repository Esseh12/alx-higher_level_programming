#!/usr/bin/python3

for n in range(1, 11):
    for x in range(1, n):
        if n % x == 0:
            print(n)
        else:
            print("not")
