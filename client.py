import random
import string
from prettytable import PrettyTable

table = PrettyTable()

def generate_output(max_num_entries):
    table.field_names = ["Name", "Mobile Number"]
    for i in range(max_num_entries):
        table.add_row([''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5, 15))), 
                       "0" + str(random.randint(100000000, 999999999))])
    choice = input("Enter your choice (1/2/3):\n1: Print to Console\n2: Save to File\n3: Both\n")
    print(table) if choice in ('1', '3') else None
    with open("output.txt", "w") as f: f.write(str(table)) if choice in ('2', '3') else None

max_num_entries = int(input("Enter the maximum number of entries: "))
generate_output(max_num_entries)

