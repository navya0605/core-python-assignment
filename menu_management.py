menu =["pizza","burger","pasta","salad"]
def add_item(menu,item):
    if item not in menu:
        menu.append(item)
        print(f"{item} is added")
    else:
        print(f"{item} is already present")
def remove_item(menu,item):
    if item in menu:
        menu.remove(item)
        print(f"{item} is removed")
    else:
        print(f"{item} is not present")
def availability(menu,item):
    if item in menu:
        print(f"{item} is available")
    else:
        print(f"{item} is not available")
def show_menu(menu):
    for item in menu:
        print(f"-{item}")
print("welcome to restaurant")
while True:
    choice=int(input("enter your choice \n 1.add item\n 2.remove\n item\n 3.availability\n 4.show menu\n"))
    if choice==1:
        item_input=input("enter item to add: ")
        add_item(menu,item_input)
    elif choice==2:
        item_input=input("enter item to remove: ")
        remove_item(menu,item_input)
    elif choice==3:
        item_input=input("enter item to check availability: ")
        availability(menu,item_input)
    elif choice==4:
        show_menu(menu)
    else:
        print("invalid choice")

