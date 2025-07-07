# Currency Converter using Functions and Default Arguments

def convert_currency(amount, from_currency='USD', to_currency='PKR'):
    # Exchange rates (for example purposes - real rates change daily)
    rates = {
        'USD': {'PKR': 278.0, 'EUR': 0.92},
        'PKR': {'USD': 0.0036, 'EUR': 0.0033},
        'EUR': {'USD': 1.09, 'PKR': 301.0}
    }

    # Check if conversion is supported
    if from_currency in rates and to_currency in rates[from_currency]:
        rate = rates[from_currency][to_currency]
        converted = amount * rate
        return round(converted, 2)
    else:
        return "Conversion rate not available."

# Example usage
print("Currency Converter")

amt = float(input("Enter amount: "))
from_curr = input("From Currency (e.g. USD, PKR, EUR): ").upper()
to_curr = input("To Currency (e.g. USD, PKR, EUR): ").upper()

result = convert_currency(amt, from_curr, to_curr)
print(f"{amt} {from_curr} = {result} {to_curr}")
