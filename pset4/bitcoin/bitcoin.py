import requests
import sys


try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    user = float(sys.argv[1])
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    response = response.json()
    bpi = float(response['bpi']['USD']['rate'].replace(",", ""))
    bitcoin = user * bpi
    print(f"${bitcoin:,.4f}")

except ValueError:
    sys.exit("Command-line argument is not a number")
except requests.RequestException:
    pass