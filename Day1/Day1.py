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
    for  i, value in enumerate(values):
        values[i] = replace_word_to_num(value)
    return part1(values)

def open_file(filename):
    # opens file and returns all strings
    with open(filename, "r") as file_input:
        input = file_input.read()
        list_of_values = input.split("\n")
        return list_of_values

def replace_all_alphabetical(string):
    # remove all alphabetical letters
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for letter in alphabet:
        string = string.replace(letter, "")
    return string

def replace_word_to_num(string):
    # replace all word numbers with number in the middle of  word
    # this is to account for overlap
    num_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    new_num_list = ['o1e', 't2o', 'th3ee', 'fo4r', 'fi5e', 's6x', 'se7en', 'ei8ht', 'ni9e']
    for i, word_num in enumerate(num_list):
        string = string.replace(num_list[i], new_num_list[i])
    return string

inputs = open_file("Day1Input")
print(part1(inputs))
print(part2(inputs))