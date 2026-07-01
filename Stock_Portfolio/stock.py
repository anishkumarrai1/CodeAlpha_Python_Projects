"""
CodeAlpha Python Internship - Task 2: Stock Portfolio Tracker
Calculates total investment value based on hardcoded stock prices.
Allows saving the result to a .txt or .csv file.
"""

import csv
from datetime import datetime

# Hardcoded dictionary of stock prices (per share, in USD)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 175,
    "MSFT": 420,
    "META": 480,
    "NFLX": 650,
    "NVDA": 120,
}


def show_available_stocks():
    print("\nAvailable stocks and prices (per share):")
    print("-" * 35)
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<8} ${price}")
    print("-" * 35)


def get_portfolio_input():
    # Collect stock names and quantities from the user.
    portfolio = {}

    show_available_stocks()
    print("\nEnter stock symbol and quantity. Type 'done' to finish.\n")

    while True:
        symbol = input("Stock symbol (e.g. AAPL): ").strip().upper()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print(f">> '{symbol}' not found in price list. Try again.\n")
            continue

        qty_input = input(f"Quantity of {symbol}: ").strip()
        try:
            quantity = int(qty_input)
            if quantity <= 0:
                print(">> Quantity must be a positive number.\n")
                continue
        except ValueError:
            print(">> Please enter a valid whole number.\n")
            continue

        # Add to existing quantity if symbol already entered
        portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        print(f">> Added {quantity} share(s) of {symbol}.\n")

    return portfolio


def calculate_investment(portfolio):
    # Calculate per-stock value and total investment.
    details = []
    total = 0
    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * quantity
        total += value
        details.append((symbol, quantity, price, value))
    return details, total


def display_summary(details, total):
    print("\n" + "=" * 50)
    print("  PORTFOLIO SUMMARY")
    print("=" * 50)
    print(f"{'Symbol':<10}{'Qty':<8}{'Price':<10}{'Value':<10}")
    print("-" * 50)
    for symbol, quantity, price, value in details:
        print(f"{symbol:<10}{quantity:<8}${price:<9}${value:<9}")
    print("-" * 50)
    print(f"TOTAL INVESTMENT: ${total}")
    print("=" * 50)


def save_to_txt(details, total, filename="portfolio_summary.txt"):
    with open(filename, "w") as f:
        f.write("STOCK PORTFOLIO SUMMARY\n")
        f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 50 + "\n")
        f.write(f"{'Symbol':<10}{'Qty':<8}{'Price':<10}{'Value':<10}\n")
        f.write("-" * 50 + "\n")
        for symbol, quantity, price, value in details:
            f.write(f"{symbol:<10}{quantity:<8}${price:<9}${value:<9}\n")
        f.write("-" * 50 + "\n")
        f.write(f"TOTAL INVESTMENT: ${total}\n")
    print(f"\n✅ Summary saved to {filename}")


def save_to_csv(details, total, filename="portfolio_summary.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Symbol", "Quantity", "Price", "Value"])
        for symbol, quantity, price, value in details:
            writer.writerow([symbol, quantity, price, value])
        writer.writerow([])
        writer.writerow(["", "", "Total", total])
    print(f"\n✅ Summary saved to {filename}")


def main():
    print("=" * 50)
    print("  STOCK PORTFOLIO TRACKER")
    print("=" * 50)

    portfolio = get_portfolio_input()

    if not portfolio:
        print("\nNo stocks entered. Exiting.")
        return

    details, total = calculate_investment(portfolio)
    display_summary(details, total)

    save_choice = input(
        "\nSave summary to file? (txt/csv/n): "
    ).strip().lower()

    if save_choice == "txt":
        save_to_txt(details, total)
    elif save_choice == "csv":
        save_to_csv(details, total)
    else:
        print("\nSummary not saved.")


if __name__ == "__main__":
    main()
      
