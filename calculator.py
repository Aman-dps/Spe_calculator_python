import math

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b  #test for subtraction

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Error! Division by zero.")
        return a / b

    @staticmethod
    def power(base, exponent):
        return math.pow(base, exponent)

    @staticmethod
    def square_root(num):
        if num < 0:
            raise ValueError("Error! Square root of a negative number.")
        return math.sqrt(num)

    @staticmethod
    def logarithm(num):
        if num <= 0:
            raise ValueError("Error! Logarithm of zero or negative number.")
        return math.log(num)

    @staticmethod
    def factorial(num):
        if num < 0:
            raise ValueError("Error! Factorial of a negative number.")
        if not float(num).is_integer():
             raise ValueError("Error! Factorial of non-integer.")
        return float(math.factorial(int(num)))

if __name__ == "__main__":
    while True:
        print("Scientific Calculator")
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
        print("5. Power\n6. Square Root\n7. Logarithm\n8. Factorial")
        print("9. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 9:
            print("Exiting the calculator...")
            break

        try:
            if choice in [1, 2, 3, 4, 5]:
                if choice == 5:
                     print("Enter base and exponent: ")
                else:
                     print("Enter two numbers: ")
                
                num1 = float(input())
                num2 = float(input())

                if choice == 1:
                    print(f"Result: {Calculator.add(num1, num2)}")
                elif choice == 2:
                    print(f"Result: {Calculator.subtract(num1, num2)}")
                elif choice == 3:
                    print(f"Result: {Calculator.multiply(num1, num2)}")
                elif choice == 4:
                    print(f"Result: {Calculator.divide(num1, num2)}")
                elif choice == 5:
                    print(f"Result: {Calculator.power(num1, num2)}")

            elif choice in [6, 7, 8]:
                print("Enter a number: ")
                num1 = float(input())

                if choice == 6:
                    print(f"Result: {Calculator.square_root(num1)}")
                elif choice == 7:
                    print(f"Result: {Calculator.logarithm(num1)}")
                elif choice == 8:
                    print(f"Result: {Calculator.factorial(num1)}")
            else:
                print("Invalid choice. Please try again.")

        except ValueError as e:
            print(e)
        except Exception as e:
             print(f"An error occurred: {e}")
