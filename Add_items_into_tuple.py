# Adding an items into the tuple by user inputs by converting it into the list and then converting it back into tuple

while(True):    
    tuple5 = tuple()
    tuple6 = list(tuple5)
    want_to_add = input("Wanna add items in the tuple: ")
    if(want_to_add.lower() == "yes"):
        while(True):
            if(want_to_add.lower() == "yes"):
                how_many_items = int(input("How many items you wanna add in the tuple: "))
                i = 0
                while i < how_many_items:
                    item = input("Enter the name of the item: ")
                    tuple6.append(item)
                    i = i + 1

                tuple7 = tuple(tuple6)
                print(f"Here's is your tuple -> {tuple7}")

                want_to_add_more = input("Wanna add more items into the tuple: ")
                if (want_to_add_more.lower() == "yes"):
                    True
                else:
                    print("Thanks for visiting.")
                    break
    else:
        print("Thanks for visiting.")
        break
    