name = "Ayush Kumar Vishwakarma"
age = 20.2323232
general = f"{name} {age:.2f} years old"

print(general)


fruit = "Banana", "apple", "Kela"
price = 23, 32, 34
i = 0
j = 0
while(i < len(fruit) and j < len(price) ):
    print(f"{fruit[i]} = {price[j]} rupees")
    i += 1
    j += 1
