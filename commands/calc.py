def calc_command():
    print("===== Calculator =====\n")
    print("Press Ctrl + C to exit the calculator.\n")

    try:
        num1 = float(input("First number: "))
        operator = input("Operator (+ - * /): ")
        num2 = float(input("Second number: "))

        operations = {
            "+": lambda: num1 + num2,
            "-": lambda: num1 - num2,
            "*": lambda: num1 * num2,
            "/": lambda: num1 / num2 if num2 != 0 else "Error: division by zero"
        }

        if operator in operations:
            print("Result:", operations[operator]())
        else:
            print("Unknown operator")

    except KeyboardInterrupt:
        print("\nReturning to AtlasOS shell...")