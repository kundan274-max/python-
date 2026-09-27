prices = []

n = int(input("Enter number of days: "))

for i in range(n):
    prices.append(int(input("Enter price: ")))

minimum = prices[0]
profit = 0

buy_day = 0
sell_day = 0

for i in range(n):

    if prices[i] < minimum:
        minimum = prices[i]
        buy_day = i

    current_profit = prices[i] - minimum

    if current_profit > profit:
        profit = current_profit
        sell_day = i

print("Maximum profit =", profit)
print("Buy price =", prices[buy_day])
print("Sell price =", prices[sell_day])
