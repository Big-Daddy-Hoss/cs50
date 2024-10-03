def main():
    greeting = input("Please type your greeting ")
    print(value(greeting))


def value(greeting):
    greeting = greeting.lower().split()

    print(greeting)

    if greeting[0] == "hello" or greeting[0] == "hello,":
        return 0
    elif greeting[0][0] == "h":
        return 20
    else:
        return 100
    

if __name__ == "__main__":
    main()
