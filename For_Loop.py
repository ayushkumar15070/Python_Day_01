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