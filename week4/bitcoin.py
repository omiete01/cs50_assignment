
import requests
import sys

if len(sys.argv) == 2:
    try:
        # converting user argument to float
        n = float(sys.argv[1])

        # storing the api request in a variable
        api_request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

        # storing the api result in a json format
        result = api_request.json()
        
        # getting the rate of USD to 1 bitcoin
        usd_rate = result.get("bpi").get("USD").get("rate_float")
        
        # multiply by user argument
        bitcoin_value = usd_rate * n

        # print the total amount to 4 decimal places
        print(f"${bitcoin_value:,.4f}")

    except ValueError:
        sys.exit("Command-line argument is not a number")
    except requests.RequestException:
        sys.exit()
else: 
    sys.exit("Missing command-line argument")


