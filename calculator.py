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
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))

        print("Addition:", calculator.add(a, b))
        print("Subtraction:", calculator.subtract(a, b))
        print("Multiplication:", calculator.multiply(a, b))
        print("Exponent:", calculator.exponent(a, b))

        if b != 0:
            print("Division:", calculator.divide(a, b))
            print("Floor division:", calculator.floor_divide(a, b))
            print("Modulus:", calculator.modulus(a, b))
        else:
            print("Division, floor division, and modulus need a non-zero second number.")

    except ValueError:
        print("Please enter valid numbers.")


if __name__ == "__main__":
    main()
