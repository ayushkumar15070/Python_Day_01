global List1
List1 = [12, 45, 7, 89, 23, 45]

#First and second element
print(List1[0])
print(List1[1])

#larger element

larger = max(List1)
print(larger)

#Smaller element
smaller = min(List1)
print(smaller)

#Average of the list items

average = 0

for i in List1:
    average = average + i

average = average / len(List1)

print(average)
#Checking if larger is 2 times the smaller or not
if (larger > (2 * smaller)):
    print(True)
else:
    print(False)

#creating a tuple
tuple1 = (List1[0], List1[1], List1[2])
print(tuple1)