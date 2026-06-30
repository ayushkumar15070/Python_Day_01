fruits = ["Apple", "Banana", "Cherry"]
for i in fruits:
    print(i)


for x in "Banana":
    print(x)

for y in fruits:
    print(y)
    if y == "Banana":
        break

for z in fruits:
    if z == "Banana":
        continue
    print(z)

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)