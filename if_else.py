a = 23
b = 34
if a > b :
    print("a is greater")
else:
    print("b is greater")

x = 12 
y = 12

if x > y:
    print("x is greater")
elif x == y:
    print("both are equal")
else:
    print("y is greater")


while(True):   
    day = int(input("Enter the day: "))

    if day <= 7: 
        if day == 1:
            print("Monday")
            break
        elif day == 2:
            print("Tuesday")
            break
        elif day == 3:
            print("Wednesday")
            break
        elif day == 4:
            print("Thursday")
            break
        elif day == 5:
            print("Friday")
            break
        elif day == 6:
            print("Saturday")
            break
        else:
            print("Sunday")
            break
    else:
        print("Enter the correct day!!")
        True


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
# if num1 > num2 : print(f"{num1} is greater than {num2}") 
print(f"{num1} is greater than {num2}") if num1 > num2 else print(f"{num2} is greater than {num1}")


num3 = num1 if num1 > num2 else num2
print(num3)