Thislist = ["Banana", "apple", "Cherry"]
for i in Thislist:
    print(i)

for i in range(len(Thislist)):
    print(Thislist[i])

i = 0
while i < len(Thislist):
    print(Thislist[i])
    i = i + 1


#Loop using loop Comprehension
[print(x) for x in Thislist]



fruits = ["Apple", "Banana", "Cherry"]
newfruits = []

for x in fruits:
    if "a" in x:
        newfruits.append(x)

print(newfruits)


# we can do the above operation within one line 

newlist = [x for x in fruits if "a" in x]
print(newlist)

# syntax => newlist = [expression for item in iterable if condition == True]

newlist2 = [x for x in fruits if x != "Apple"]
print(newlist2)

# list1 = [x for x in fruits]
list1 = [x for x in range(10)]
list2 = [x for x in range(10) if x > 3]
list3 = [x.upper() for x in fruits]
list4 = ["Hello" for x in fruits]
list5 = [x if x != "Banana" else "orange" for x in fruits]
print(list5)
print(list4)
print(list3)
print(list2)

print(list1)