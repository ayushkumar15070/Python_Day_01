thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(thistuple[0])
# thistuple[0] = "kiwi" #we cannot do this in tuple
print(thistuple)


if "apple" in thistuple:
    print("Yes apple is present in the tuple.")
else:
    print("No apple is not present in the tuple.")


# we can change the value in the tuple by first converting it into list and then into tuple again

x = ("Cars", "Athletes", "Sportsbike")
y = list(x)
y[1] = "Virat Kohli"
x = tuple(y)

print(x)


z = ("BMW",)
x += z
print(x)

# we cannot remove an item directly from tuple but we can do it by first changing it into list and then remove and then again convert it to tuple

v = list(x)
v.remove("BMW")
print(v)

#unpacking of tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green, yellow, red)


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)


(green, *yellow, red ) = fruits
print(green)
print(yellow)
print(red)


for i in fruits:
    print(i)

i = 0
while i < len(fruits):
    print(fruits[i])
    i = i + 1