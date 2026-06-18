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