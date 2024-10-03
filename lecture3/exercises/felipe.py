menu = {

    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00

    }

menu_items = ""

for item in menu:
    menu_items += f"{item}, "

menu_items = menu_items.strip(menu_items[-2:])



def main():
    print(take_order())
   # print(menu_items)



def take_order():
    total_order = None
    total_price = 0

    while True:
        try:
            order = (input(f"Please order an item from the menu- {menu_items}:  ").lower()).title()
            
            if order == "None":
                return (f"Your total is ${total_price:.2f}")
            
            else:
                total_price += menu[order]

        except KeyError:
            print("Not found, please only pick an item from the menu")
    
        #else:
          #  return (f"Your total is{total_price}")
main()