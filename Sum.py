num = int(input("Enter the number: "))
original = num
sum = 0
while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10

print(f"The sum of the digit {original} is {sum}")
