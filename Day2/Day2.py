import re

def open_file(filename):
    # opens file and returns all strings
    with open(filename, "r") as file_input:
        input = file_input.read()
        list_of_values = input.split("\n")
        return list_of_values


def part1(values, red, green, blue):
    total_id = 0
    current_id = 0
    for value in values:
        deconstruction = value.split((": "))
        current_id = deconstruction[0][5]
        grab_attempts = deconstruction[1].split(";")
        for attempt in grab_attempts:
            re.findall()
            print(attempt)
        print()

    return total_id

def determine_possible():
    print()

inputs = open_file("Day2Input")

print(part1(inputs, 12, 13, 14))
