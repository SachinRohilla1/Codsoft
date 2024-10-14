
import random
import string
from prettytable import PrettyTable

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

def generate_random_number(length):
    if length == 1:
        return random.randint(0, 9)
    return int(str(random.randint(10**(length-1), 10**length - 1)).lstrip('0'))

def generate_sales_data(num_entries):
    table = PrettyTable()
    table.field_names = ["Product Name", "Price", "Quantity Sold", "Revenue"]
    for i in range(num_entries):
        name = generate_random_name(random.randint(1, 10))
        price = round(generate_random_number(3) + random.random(), 2)
        quantity = generate_random_number(2)
        revenue = price * quantity
        table.add_row([name, price, quantity, revenue])
    return table

# Input validation
while True:
    try:
        num_entries = int(input("Enter the number of entries (1-1000): "))
        if 1 <= num_entries <= 1000:
            break
        else:
            print("Please enter a number between 1 and 1000.")
    except ValueError:
        print("Invalid input. Please enter a number.")

sales_data = generate_sales_data(num_entries)

# Save output to a text file
with open("sales_data.txt", "w") as f:
    f.write(str(sales_data))

print("Data saved to sales_data.txt")

