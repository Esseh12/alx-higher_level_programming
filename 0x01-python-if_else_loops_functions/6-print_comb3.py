#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        print("{:02d}, {:02d}".format(i, j), end=", " if j < 9 else "{:02d}, {:02d}\n".format(i, j))
