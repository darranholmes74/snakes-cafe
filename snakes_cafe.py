menu = {
    "Wings": 0, "Cookies": 0, "Spring Rolls": 0,
    "Salmon": 0, "Steak": 0, "Meat Tornado": 0, "A Literal Garden": 0,
    "Dessert": 0, "Ice Cream": 0, "Cake": 0, "Pie": 0,
    "Coffee": 0, "TeaUnicorn": 0, "Tears": 0
}


intro = ("""
    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **
    ** To quit at any time, type "quit" **
    **************************************
    
    Appetizers
    ----------
    Wings
    Cookies
    Spring Rolls

    Entrees
    -------
    Salmon
    Steak
    Meat Tornado
    A Literal Garden

    Desserts
    --------
    Ice Cream
    Cake
    Pie

    Drinks
    ------
    Coffee
    Tea
    Unicorn Tears

    ***********************************
    ** What would you like to order? **
    ***********************************
    
    """)


def print_intro():
    print(intro)

    while True:
        menu_item = input("> ").lower()
        if menu_item.lower() == "quit":
            print("Thanks for stopping by")
            break
        menu_item = menu_item.title()
        if menu_item not in menu.keys():
            print("Sorry, we don't sell that here")

        else:
            menu[menu_item] += 1
            if menu[menu_item] == 1:
                print(f"** {menu[menu_item]} order of {menu_item} have been added to your meal **")
            else:
                print(f"** {menu[menu_item]} order of {menu_item} have been added to your meal **")


if __name__ == "__main__":
    print_intro()
