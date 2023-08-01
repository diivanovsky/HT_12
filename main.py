# 1 Task
def imt_count():
    try:
        weight = int(input("Enter your weight in kilos: "))
        height = int(input("Enter your height in centimetres: "))
        if weight and height < 1:
            raise ZeroDivisionError
        imt = round((weight / ((height / 100) ** 2)), 1)
        if imt < 16.5:
            print(f"Your index is: {imt}. It's huge underweight, so close to death")
        elif 16 < imt < 18.6:
            print(f"Your index is: {imt}.It's underweight")
        elif 18.5< imt < 26:
            print(f"Your index is: {imt}. It's normal weight")
        elif 24 < imt < 31:
            print(f"Your index is: {imt}. It's overweight")
        elif 29 < imt < 35:
            print(f"Your index is: {imt}. It's obesity (First class)")
        elif 34 < imt < 40:
            print(f"Your index is: {imt}. It's obesity (Second class - severe)")
        elif 40 < imt:
            print(f"Your index is: {imt}. It's obesity (Second class - very severe)")
    except ValueError:
        print("Enter only numbers, without coma")
        return imt_count()
    except ZeroDivisionError:
        print("You be zero in your life but not in numbers")
        return imt_count()


imt_count()


# 2 Task
class Calculator:
    def summ(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mult(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            raise ZeroDivisionError
        return a / b


calc = Calculator()

while True:
    try:
        operator = input('Choose an operation: \n 1. Add. \n 2. Subtract. \n 3. Multiply. \n 4. Divide. \n 5. Exit. \n')
        a = float(input('Enter the first number: '))
        b = float(input('Enter the second number: '))

        if operator == '1':
            result = calc.summ(a, b)
        elif operator == '2':
            result = calc.sub(a, b)
        elif operator == '3':
            result = calc.mult(a, b)
        elif operator == '4':
            result = calc.div(a, b)
        elif operator == '5':
            break
        else:
            raise ValueError

        print('THe result is:', result)

    except ValueError as ve:
        print('Error:', ve, "Try to enter only numbers")

    except ZeroDivisionError as zde:
        print("Error:", zde, "You can't divide by zero")