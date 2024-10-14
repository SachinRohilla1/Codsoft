a = int (input('Enter your first number: '))
b = int (input('Enter your second number: '))



print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1, 2, 3, 4): "))

match choice:
    case 1:
        print(a + b)
    case 2:
        print(a - b)
    case 3:
        print(a * b)
    case 4:
            print(a // b)
    case _:
        print("Invalid choice")

