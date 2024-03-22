def max_profit(prices):
    n = len(prices)
    if n <= 1:
        return 0

    # Initialize arrays to store maximum profit with 1 transaction and 2 transactions
    max_profit_1 = [0] * n
    max_profit_2 = [0] * n

    # Calculate maximum profit with 1 transaction
    min_price = prices[0]
    for i in range(1, n):
        min_price = min(min_price, prices[i])
        max_profit_1[i] = max(max_profit_1[i - 1], prices[i] - min_price)

    # Calculate maximum profit with 2 transactions
    max_price = prices[n - 1]
    for i in range(n - 2, -1, -1):
        max_price = max(max_price, prices[i])
        max_profit_2[i] = max(max_profit_2[i + 1], max_price - prices[i])

    # Calculate maximum profit overall
    max_profit = 0
    for i in range(n):
        max_profit = max(max_profit, max_profit_1[i] + max_profit_2[i])

    return max_profit

# Example usage
stock_prices = [7,1,5,3,6,4]
result = max_profit(stock_prices)
print("Maximum profit:", result)
