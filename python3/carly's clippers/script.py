hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Create total_price variable
total_price = 0

# Create for loop to sum total price
for price in prices:
  total_price += price

# Create average_price variable
average_price = total_price / len(prices)

# Print average_price
print(average_price)

# Reduce all prices by 5
new_prices = [price -5 for price in prices]

# Print new_prices
print(new_prices)

# Create total_revenue variable
total_revenue = 0

# Create for loop for total revenue calculation
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]

# Print total_revenue
print("Total Revenu:", total_revenue)

# Create and print out average_daily_revenue
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

# Create cuts_under_30 variable
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print(cuts_under_30)
