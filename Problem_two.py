num1 = "25"
num2 = "40"

print("Without casting: " + num1 + num2)

num3 = int(num1)
num4 = int(num2)
print(f"After casting: {num3 + num4}")

print(f"Product: {num3 * num4}")
print("Type of product string:", type(num1))