#print("What's your name? ")

def hello(to = "world"):  #assigns default value
    print("hello,", to)

def main():
    name = input("What's your name? ")
    name = name.strip().title()

hello(name)

def hello(to = "world"):  #assigns default value
    print("hello,", to)

main()
#first, last = name.strip()
#print("Hello,", name, sep =" ") 


