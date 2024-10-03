def main():
    print(get_coke())

def get_coke():
    total_paid = 0

    while total_paid < 50:
        payment = int(input("Please choose either 5, 10, or 25 "))
        total_paid += payment

    change = str(total_paid - 50)

    return "Your change is: " + change

main()