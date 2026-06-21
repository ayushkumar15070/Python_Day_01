thisset = {"Apple", "Banana", "Cherry"}
for i in thisset:
    print(i)


#joining the sets by using union, intersection and many more

set1 = {"A", "B", "C"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

set4 = set1 | set2
print(set4)


set5 = {"Ayush", "Vishal", "Arush"}
set6 = {"BMW", "Mercedes", "Range Rover"}

set7 = set1.union(set2, set5, set6)
print(set7)

# or

set8 = set1 | set2 | set5 | set6
print(set8)

# Tuple and Set joining 

set9 = (4, 5, 6, 3)
set10 = set2.union(set9)
print(set10)

set12 = {2, 3, 4, 5, 6}

set11 = set2.intersection(set9)
print(set11)

set11 = set2 & set12
print(set11)


# Intersection Update
set2.intersection_update(set12)
print(set2)

#Difference 

set13 = set2.difference(set12)
print(set13)

set14 = {"apple", "banana", "cherry"}
set15 = {"banana", "apple", "kiwi"}
set16 = set14 - set15
print(set16)

set14.difference_update(set15)
print(set14)
set17 = set14.symmetric_difference(set15)
print(set17)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)


#frozenset

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
