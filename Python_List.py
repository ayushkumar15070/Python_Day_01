#List 

fruits = ["apple", "banana", "cherry"]
print(fruits)
print(len(fruits))

list1 = ["apple", "fruits", "cherry"]
list2 = [1, 2, 3, 4]
list3 = [True, False, True, False]


list4 = ["apple", 34, "reddish", "Kashmiri"]
print(type(list4))

list5 = list(("Apple", "Banana", "Cherry"))
print(list5)

print(list4[2])

#Negative indexing 
print(list4[-2])

#range 
print(list4[1:3])

name = input("Enter the name of a fruit: ")
if name in list1:
    print(f"The Fruit {name} is present in the list {list1} at index of 0")
else:
    print(f"The Fruit {name} is not present in the list {list1}")