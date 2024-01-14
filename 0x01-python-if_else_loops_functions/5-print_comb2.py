#!/usr/bin/python3
for i in range(0, 100):
    if i in range(0, 10):
        print(f"0{i}, ", end= "")
    else:
        print(f"{i}, \n", end= "")
