list1 = ["Kiwi", "Papaya", "Banana", "Cherry", "Nothing", "Fruit"]

list1.sort()
print(list1)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


List2 = [1, 4, 5, 9, 2, 34, 3, 12, 2323, 121, 2]
List2.sort()
List2.sort(reverse=True)
print(List2)


#Customize sort function

def myfunct(n):
    return abs(n - 50)

list3 = [ 100, 20, 30, 40, 21]
list3.sort(key = myfunct)
print(list3)


list4 = ["Apple", "Banana", "Cherry"]
list4.reverse()
print(list4)

#Copying a list 

list5 = list4.copy()
print(list5)

list6 = list(list5)
print(list6)

list7 = list6[:]
print(list7)