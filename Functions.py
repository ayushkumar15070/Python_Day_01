def myfunction():
    print("This is a function.")


myfunction()


def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1/ num2

calculation = input("Want to perform any calculation: ")

while(True):
    if( calculation.lower() == "yes"):
        calculator = int(input("""-----------Calculator-------------
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Division
                            
        """))
        match calculator:
            case 1:
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))
                result = addition(num1, num2)
                print(result)
                
            case 2:
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))
                result = subtraction(num1, num2)
                print(result)
            case 3:
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))
                result = multiplication(num1, num2)
                print(result)
            case 4:
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))
                result = division(num1, num2)
                print(result)

        another = input("Want to perform any other calulation: ")
        if(another.lower() == "yes"): 
            True
        else:
            print("Thank you for visiting")
            break
    else:
        print("Thank you for visiting")
        break



