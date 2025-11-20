import re

def part1(inputs):
    total = 0
    for value in inputs:
        num1 = re.search(r"d+", value)
        print(num1)
    print(inputs)

def open_file(filename):
    with open(filename, "r") as file_input:
        input = file_input.read()
        list_of_values = input.split("\n")
        return list_of_values

file_input = open_file("Day1Input")
part1(file_input)