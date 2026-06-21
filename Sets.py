Thisset = {"apple", "banana", "cherry"}
print(Thisset)
print(type(Thisset))

set1 = {"cars", "athletes", "cricketers", "footballers"}
set2 = {True, False}
set3 = {1, 2, 3, 4, 5}
print(set1)
print(set2)
print(set3)

for i in Thisset:
    print(i)

if "banana" in Thisset:
    print("Yes, banana is present in the set")
else:
    print("No, banana is not preset in the set")

if "cars" not in set1:
    print("No, the cars is not present in set1")
else:
    print("Yes, the cars is present in set1")


#Addint an item inside the set

set4 = {"Apple", "Banana", "Cherry"}
newitem = input("Enter the item name which you want to add in the set: ")
set4.add(newitem)
print(set4)


#Adding the items of another set to the set
set5 = {"Pineapple", "Guava", "Grapes"}
set4.update(set5)
print(set4)