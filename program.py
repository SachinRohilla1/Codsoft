import random
import string
from prettytable import prettytable
def generate_random_name(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def generate_random_number(length):
    return random.randint(10**(length-1), 10**length - 1)

def generate_output(num_entries, name_length, num_length):
    output = []
    for i in range(num_entries):
        name = generate_random_name(name_length)
        num = generate_random_number(num_length)
        output.append(f"{name}={num}")
    with open("output.txt", "w") as f:
        f.write(' '.join(output))

print(generate_output(1024, 6, 3))
