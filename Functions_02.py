def my_function(*fruits):
    print("The yellow fruits is", fruits[1])



my_function("Apple", "Banana", "Cherry")


def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")


number = int(input("Enter the size of number which you want to add: "))
num = []
for i in range(number):
   numbers = int(input("Enter the number"))
   num.append(numbers)

newnum = tuple(num)

def add(*newnum):
   total = 0
   for i in newnum:
      total = total + newnum

   return total

print(add(newnum))
    