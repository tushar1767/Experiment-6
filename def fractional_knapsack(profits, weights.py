def fractional_knapsack(profits, weights, capacity):
    n = len(profits)

    # Calculate profit-to-weight ratio
    items = [
        (profits[i], weights[i], profits[i] / weights[i])
        for i in range(n)
    ]

    # Sort items by ratio in descending order
    items.sort(key=lambda item: item[2], reverse=True)

    total_profit = 0.0
    remaining = capacity

    for profit, weight, ratio in items:
        if remaining <= 0:
            break

        if weight <= remaining:
            # Take the complete item
            total_profit += profit
            remaining -= weight
        else:
            # Take only the fraction that fits
            fraction = remaining / weight
            total_profit += profit * fraction
            remaining = 0

    return total_profit


# Given data
profits = [25, 24, 15]
weights = [18, 15, 10]
capacity = 20

# Call the function
maximum_profit = fractional_knapsack(
    profits, weights, capacity
)

print("Maximum profit:", maximum_profit)