# Your code below:
# Create toppings list
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
print(toppings)

# Create price list
prices = [2, 6, 1, 3, 2, 7, 2]
print(prices)

# Count 2 dollar slices
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

# Sort toppings list
num_pizzas = len(toppings)
print(num_pizzas)

# Print a specific string
print("We sell", num_pizzas, "different kinds of pizza!")

# Create 2D list
pizzas_and_prices = [
  [2, "pepperoni"],
  [6, "pineapple"],
  [1, 'cheese'],
  [3, 'sausage'],
  [2, 'olives'],
  [7, 'anchovies'],
  [2, 'mushrooms']
]
print(pizzas_and_prices)

# Sort pizzas_and_prices by price
pizzas_and_prices.sort()
print(pizzas_and_prices)

# Store cheapest_pizza
cheapest_pizza = pizzas_and_prices[0]
print(cheapest_pizza)

# store priciest_pizza
priciest_pizza = pizzas_and_prices[-1]
print(priciest_pizza)

# remove anchovi pizza
pizzas_and_prices.pop()
print(pizzas_and_prices)

# add peppers pizza
pizzas_and_prices.insert(4, [2.5, "peppers"])
print(pizzas_and_prices)

# slice cheapest slices
three_cheapest = pizzas_and_prices[:3]
print(three_cheapest)
