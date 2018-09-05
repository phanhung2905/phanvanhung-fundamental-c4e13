menu_items = ["T-shirt", "sweater"]
print(menu_items)
count = 0
loop = True
while loop:
    command = input("welcome to our shop, what do you want(C, R, U, D)").upper()

    if command == "R":
        print("our items:", menu_items)

    elif command == "C":
        fav = input("enter the item you like: ")
        menu_items.append(fav)
        print("our items:", menu_items)
    
    elif command == "U":
        position = int(input("update position? : ")) - 1 
        update_menu = input("new item? : ")
        menu_items[position] = update_menu
        print("our item", menu_items)

    elif command == "D":
        position = int(input("delete position: ")) -1
        menu_items.pop(position)
        print("our item:", menu_items)
    else:
        print("nothing")
        loop = False



    




