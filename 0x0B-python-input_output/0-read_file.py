#!/usr/bin/python3
def read_file(filename=""):
    with open("my_file_0.txt", encoding="UTF8") as my_file:
        read_data = my_file.read()
        print(read_data.strip())
