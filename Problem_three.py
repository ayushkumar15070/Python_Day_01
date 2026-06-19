name = input("Enter your name: ")
age  = int(input("Enter your age: "))

print(name.upper())
print(f"Your age after 5 years {age + 5}")

if(age> 18):
    print(True)
else:
    print(False)