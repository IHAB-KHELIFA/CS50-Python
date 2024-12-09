import sys
import requests

def main():
    # Check and parse command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python bitcoin.py <amount>")

    # Try to convert the argument to a float
    try:
        amount = float(sys.argv[1])
    except ValueError:
        sys.exit("Error: Amount must be a number.")

    # Fetch the current price of Bitcoin in USD
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        bitcoin_price = data["bpi"]["USD"]["rate_float"]
    except requests.RequestException:
        sys.exit("Error: Could not fetch Bitcoin price.")
    except (KeyError, TypeError):
        sys.exit("Error: Unexpected response format from API.")

    # Calculate the total cost
    total_cost = bitcoin_price * amount

    # Output the result formatted to four decimal places with thousands separator
    print(f"${total_cost:,.4f}")

if __name__ == "__main__":
    main()
