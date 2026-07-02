def my_function(*fruits):
    print("The yellow fruits is", fruits[1])



my_function("Apple", "Banana", "Cherry")


def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")
    

def my_function2(*numbers):
  if len(numbers) == 0:
    return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num

print(my_function2(3, 7, 2, 9, 1))


def function(**dog):
  print("The dog name is " + dog["name"])

function(name = "Reo", anothername = "Leo")

def my_function3(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function3("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

