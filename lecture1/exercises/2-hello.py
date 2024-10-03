def main():
    print(greetingCheck())


def greetingCheck():
    greeting = input("Please type your greeting ")
    greeting = greeting.lower().split()

    print(greeting)

    if greeting[0] == "hello" or greeting[0] == "hello,":
        return "$0"
    elif greeting[0][0] == "h":
        return "$20"
    else:
        return "$100"
    

main()