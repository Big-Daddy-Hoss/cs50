from collections import Counter

def main():
    get_grocery_list()

def get_grocery_list():
    
    grocery_list = []
    final_list = []

    while True:
            try:
                item = input("Pleast choose an item for the grocery list   ").lower().title()
                grocery_list.append(item)

            except EOFError:
                break
    
    item_count = Counter(grocery_list)
    #print(grocery_list)
    #print(item_count)

    for items in item_count:
        print(item_count[items], items)        

    

 
main()