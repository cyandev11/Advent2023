from contextlib import nullcontext


def part1(values):
    total = 0
    for value in values:
        updated_value = replace_all_alphabetical(value)
        if len(updated_value) > 0:
            first_num = updated_value[0]
            second_num = updated_value[-1]
            final_num = int("" + first_num + "" + second_num)
            total += final_num
    return total

def part2(values):
    print('part2')

def open_file(filename):
    with open(filename, "r") as file_input:
        input = file_input.read()
        list_of_values = input.split("\n")
        return list_of_values

def replace_all_alphabetical(string):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for letter in alphabet:
        string = string.replace(letter, "")
    return string

def replace_word_to_num(string):
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for number in numbers:
        string = string.replace(number, "")
    return string

inputs = open_file("Day1Input")
print(part1(inputs))