import requests
import sys
import json


def main():
    get_price()


def get_price():
    if len(sys.argv) != 2:
        sys.exit()

    try:
        number_of_btc = float(sys.argv[1])
        price = requests.get(
            "https://api.coindesk.com/v1/bpi/currentprice.json"
        )  # ["bpi"]["USD"]["rate_float"]
        # print(price.json())

        usd_price = price.json()["bpi"]["USD"]["rate_float"]

        total_price = usd_price * number_of_btc

    except TypeError or ValueError or AttributeError:
        sys.exit()

    print(f"{total_price:,}")


main()
