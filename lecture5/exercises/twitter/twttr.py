def main():
    word = input("Please type a string:  ")
    print(shorten(word))



def shorten(word):
    word_list = [*word] 
    new_word = "" 
    for letter in word_list:
        if letter not in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            new_word += letter
        else:
            pass
    return new_word.strip()


if __name__ == "__main__":
    main()
