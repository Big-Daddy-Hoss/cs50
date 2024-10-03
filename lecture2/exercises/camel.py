def main():

    print(convert_to_camel())

def convert_to_camel():
    teststring = input("Please input camelcase string ")
    snake_string = ""

    for character in teststring:
        if character.islower():
            snake_string += character

        else:
            snake_string += ("_" + character.lower())

    return snake_string

main()