
import random
import string
from prettytable import PrettyTable
import datetime

# Function to generate random names
def generate_random_name(length, max_length=20):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    name = ''
    for i in range(length):
        if i % 2 == 0:
            name += random.choice(consonants)
        else:
            name += random.choice(vowels)
    return name[:max_length]

# Function to generate random numbers
def generate_random_number(length):
    return int(str(random.randint(10**(length-1), 10**length - 1)).lstrip('0'))

# Function to generate output
def generate_output(max_num_entries, max_name_length, max_num_length):
    num_entries = random.randint(1, max_num_entries)
    name_length = random.randint(1, max_name_length)
    num_length = random.randint(1, max_num_length)
    table = PrettyTable()
    table.field_names = ["Name", "Number"]
    table.align["Name"] = "l"
    table.align["Number"] = "r"
    for i in range(num_entries):
        name = generate_random_name(name_length)
        num = generate_random_number(num_length)
        table.add_row([name, num])
    with open("output.txt", "w") as f:
        f.write("Random Names and Numbers\n\n")
        f.write(str(table))
        f.write("\n\nGenerated on: " + str(datetime.datetime.now()))

# Get user input
max_num_entries = int(input("Enter the maximum number of entries: "))
max_name_length = int(input("Enter the maximum length of the names: "))
max_num_length = int(input("Enter the maximum length of the numbers: "))

# Call the function with user input
generate_output(max_num_entries, max_name_length, max_num_length)




