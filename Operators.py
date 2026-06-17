#Python operators

x = 127
y = 23
print(x + y)
print(x * y)
print(x - y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

x = 5
x = x & 3
print(x)
x = x | 3
print(x)
# Walrus operator
if (length := len(input("Enter your name: "))) > 5:
    print("Long name")
    print(length)