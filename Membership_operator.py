x = [1, 2, 3, 4]
y = 2 in x
print(y)

fruits = []
first = input("Enter the name of a fruit: ")
fruits.append(first)
second = input("Enter the name of a fruit: ")
fruits.append(second)
third = input("Enter the name of a fruit: ")
fruits.append(third)

banana = "banana" in fruits
print(banana)
banana = "pineapple" not in fruits
print(banana)


#Membership in strings 

hello = "Hello, World!"
s = "H" in hello
print(s)