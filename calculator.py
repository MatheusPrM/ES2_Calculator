def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def menu():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit")
    choice = input("Enter your choice: ")
    return choice


def get_numbers():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    return a, b


def calculate():
    a, b = get_numbers()
    if choice == "1":
        print(add(a, b))
    elif choice == "2":
        print(subtract(a, b))
    elif choice == "3":
        print(multiply(a, b))
    elif choice == "4":
        print(divide(a, b))


while True:
    choice = menu()
    if choice == "5":
        break
    calculate()

if __name__ == "main":
    calculate()