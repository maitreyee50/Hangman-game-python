stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 310
}
print("Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))

portfolio = {}
total_value = 0

while True:
    stock = input("Enter stock symbol (or type 'done' to finish): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("Stock not found. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        if quantity < 0:
            print("Quantity cannot be negative.")
            continue
        portfolio[stock] = quantity
        investment = stock_prices[stock] * quantity
        total_value += investment
    except ValueError:
        print("Please enter a valid number.")


print("\n Portfolio Summary:")
for stock, qty in portfolio.items():
    print(f"{stock}: {qty} shares @ ${stock_prices[stock]} = ${qty * stock_prices[stock]}")
print(f"\n Total Investment Value: ${total_value}")

save = input("\nDo you want to save the result to a file? (yes/no): ").lower()
if save == "yes":
    file_type = input("Choose file type (.txt or .csv): ").lower()
    filename = "portfolio_result" + (".csv" if file_type == ".csv" else ".txt")
    with open(filename, "w") as file:
        file.write("Stock,Quantity,Price per Share,Total Value\n")
        for stock, qty in portfolio.items():
            file.write(f"{stock},{qty},{stock_prices[stock]},{qty * stock_prices[stock]}\n")
        file.write(f"\nTotal Investment Value: ${total_value}")
    print(f"Portfolio saved to {filename}")
