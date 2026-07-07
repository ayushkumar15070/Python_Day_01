import mymodule

mymodule.greetings("Ayush")


Talent = mymodule.person1["Talent"]
print(Talent)
print(mymodule.person1["Age"])


# Renaming a module

import Another_module as addition


num1 = int(input("Enter the number: "))
num2 = int(input("Enter the number: "))
addition.addition(num1, num2)


import platform

x =platform.processor()
print(x)


from Another_module import person2

Hidden_Talent = person2["Hidden Talent"]
print(Hidden_Talent)
