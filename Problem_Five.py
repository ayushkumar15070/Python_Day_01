name = input("Enter your name: ")
marks = list()
for i in range(0, 3):
    sublist = ["Science", "Maths", "English"]
    markinput = float(input(f"Enter your {sublist[i]} Marks: "))
    marks.append(markinput)

average = (marks[0] + marks[1] + marks[2]) / 3 

print(f"Name of the Student is -> {name.upper()}")
print(f"The Average marks of {name} is -> {average:.2f} ")

if(average >= 60):
    print(True)
else:
    print(False)

tuplemarks = tuple(marks)
print(tuplemarks)
