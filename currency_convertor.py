import requests

# Function to fetch exchange rates from a free API (https://exchangeratesapi.io/)
def get_exchange_rates(base_currency):
    try:
        url = f"https://api.exchangerate-api.com/v4/latest/USD?base={base_currency}"
        response = requests.get(url)
        data = response.json()
        return data["rates"]
    except Exception as e:
        print(f"Error fetching exchange rates: {e}")
        return None

# Function to convert currency
def convert_currency(amount, from_currency, to_currency, exchange_rates):
    if from_currency == to_currency:
        return amount

    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        print("Invalid currency code.")
        return None

    rate = exchange_rates[to_currency]
    converted_amount = amount * rate
    return converted_amount

# Outside Function

base_currency = input("Enter the base currency (e.g., USD, EUR, INR): ").upper()
amount = float(input("Enter the amount to convert: "))
to_currency = input("Enter the target currency (e.g., USD, EUR, INR): ").upper()

exchange_rates = get_exchange_rates(base_currency)

if exchange_rates:
    converted_amount = convert_currency(amount, base_currency, to_currency, exchange_rates)
    if converted_amount is not None:
        print(f"{amount} {base_currency} is equal to {converted_amount:.2f} {to_currency}")

