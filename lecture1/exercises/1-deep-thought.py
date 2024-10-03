def main():
    print(deepThought())

def deepThought():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")                
    if answer in ("42", "forty two", "forty-two"):
        return "Yes"
    else:
        return "No"


main()