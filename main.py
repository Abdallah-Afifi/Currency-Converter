from forex_python.converter import CurrencyRates

def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()
    
    try:
        exchange_rate = c.get_rate(from_currency, to_currency)
        converted_amount = amount * exchange_rate
        return converted_amount
    except Exception as e:
        print(f"Error converting currency: {e}")
        return None

def main():
    print("Welcome to the Currency Converter!")

    amount = float(input("Enter the amount to convert: "))
    from_currency = input("Enter the source currency code (e.g., USD): ").upper()
    to_currency = input("Enter the target currency code (e.g., EUR): ").upper()

    converted_amount = convert_currency(amount, from_currency, to_currency)

    if converted_amount is not None:
        print(f"{amount:.2f} {from_currency} is equal to {converted_amount:.2f} {to_currency}.")

if __name__ == "__main__":
    main()
