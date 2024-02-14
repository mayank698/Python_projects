from calculator_art import logo

def add(n1, n2):
    return n1+n2


def subtract(n1, n2):
    return n1-n2


def multiply(n1, n2):
    return n1*n2


def divide(n1, n2):
    return n1/n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print(logo)

def calculator():
    num1 = float(input("Enter first number: "))

    for key in operations:
        symbols = key
        print(symbols)

    END = True

    while END:
        operation_symbol = input("Enter symbol from the above list: ")
        num2 = float(input("Enter second number: "))
        calculation = operations[operation_symbol]
        answer1 = calculation(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer1}")

        if input(f"Type 'y' to continue, or type 'n' to start new calculation: ") == 'y':
            num1 = answer1
        else:
            END = False
            calculator()


calculator()
