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

#Changing the values in the list

cars = ["BMW", "Mercedes", "Audi", "Volvo", "TATA"]
cars[2] = "Saburo"

for i in range(len(cars)):
    print(cars[i])
else:
    print("Nothing is there")


thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)


#insert method

Aeroplanes = ["Gulfstrem101", "Boeing777", "Gulfstream404", "NanoBanana"]
fortuner = input("Enter any name of a fortuner car: ")
Aeroplanes.insert(3, fortuner)
print(Aeroplanes)



#Append Method
Fruits = []
Fruit1 = input("Enter any fruit name: ")
Fruit2 = input("Enter any fruit name: ")
Fruit3 = input("Enter any fruit name: ")
Fruit4 = input("Enter any fruit name: ")

Fruits.append(Fruit1)
Fruits.append(Fruit2)
Fruits.append(Fruit3)
Fruits.append(Fruit4)

print(Fruits)



#Extend Method

Cricketers = ["Virat Kohli", "MSD", "ABD", "Rohit Sharma"]
Footballer = ["Christiano Ronaldo", "Lionel Messo", "Haland", "Zidane"]
Actors = ("Robert Downey Jr.", "Chris Evans", "Mark Raffalo", "Tom Cruise")

Cricketers.extend(Footballer)
print(Cricketers)


# By using the Extend method we can add any of the type of iterables including dict, sets, tuple
Cricketers.extend(Actors)
print(Cricketers)




# Removing Methods

Planets = ["Earth", "Sun", "Pluto", "Jupiter"]
Planets.remove("Earth")
print(Planets)

#pop

Planets.pop(1)
print(Planets)

#del

del Planets


Planets = ["Nothing", "anything", "Something", "Everything", "Anything"]
Planets.clear()
print(Planets)