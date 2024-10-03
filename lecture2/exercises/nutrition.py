def main(): 

    nutrition_facts = [
        {"fruit": "apple", "Calories": 130},
        {"fruit": "avocado", "Calories": 50},
        {"fruit": "banana", "Calories": 110},
        {"fruit": "cantaloupe", "Calories": 50},
        {"fruit": "grapefruit", "Calories": 60},
        {"fruit": "apple", "Calories": 80}

        ]   

    selection = (input("Please select a fruit ")).lower()


    for i in  range (len(nutrition_facts)):
        if nutrition_facts[i]["fruit"] == selection:
            #nutrition_facts.remove(item)
            print("Calories " + str(nutrition_facts[i]["Calories"]))
            print(i)
        elif i == len(nutrition_facts) - 1:
            print("Fruit not found, please try again!")

 

        


main()