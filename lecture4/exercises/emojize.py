import emoji
import sys

def main():
    convert_to_emoji()



def convert_to_emoji():
    try:
      print(emoji.emojize(f"{sys.argv[1]}"))

    except TypeError:
       sys.exit

    


main()