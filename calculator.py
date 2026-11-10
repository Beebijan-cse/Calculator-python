import math


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

    def floor_divide(self, a, b):
        return a // b

    def modulus(self, a, b):
        return a % b

    def exponent(self, a, b):
        return a ** b


def main():
    calculator = Calculator()

    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    if not math.isfinite(first_number) or not math.isfinite(second_number):
        print("Please enter normal, finite numbers.")
        return

    print("Addition:", calculator.add(first_number, second_number))
    print("Subtraction:", calculator.subtract(first_number, second_number))
    print("Multiplication:", calculator.multiply(first_number, second_number))

    if second_number == 0:
        print("Division, floor division, and modulus need a non-zero second number.")
    else:
        print("Division:", calculator.divide(first_number, second_number))
        print("Floor division:", calculator.floor_divide(first_number, second_number))
        print("Modulus:", calculator.modulus(first_number, second_number))

    try:
        print("Exponentiation:", calculator.exponent(first_number, second_number))
    except OverflowError:
        print("That exponent result is too large to calculate.")


if __name__ == "__main__":
    main()
