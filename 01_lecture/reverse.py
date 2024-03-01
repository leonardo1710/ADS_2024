"""
Analyse the code below and try to find out what it does!

Even though you don't know a lot of the keywords yet, you might be able to understand what's going on by reading the
code line by line. To start out, you can try to "translate" the code in natural language.
"""

groceries = [
    ["Apple", 5, 0.45],
    ["Banana", 8, 0.80],
    ["Onion", 4, 0.70],
    ["Milk", 1, 1.90],
    ["Bread", 2, 3.50],
    ["Fish", 2, 16.90],
    ["Cake", 1, 12.60],
    ["Steaks", 4, 9.95],
]

sum_total = 0
items_total = 0
cheap_items_count = 0
normal_items_count = 0
expensive_items_count = 0

for item in groceries:
    name, qty, price = item

    items_total = items_total + qty

    sum_total = sum_total + (qty * price)

    if price > 0 and price <= 4.99:
        cheap_items_count = cheap_items_count + qty
    elif 4.99 < price <= 14.99:
        normal_items_count = normal_items_count + qty
    else:
        expensive_items_count = expensive_items_count + qty

average_price = sum_total / items_total
average_price = round(average_price, 2)

total_sum_as_string = str(sum_total)

print("Total sum to pay: " + total_sum_as_string + " €")
print("The average price is " + str(average_price) + " € per item.")
print("Amount of cheap items bought:", cheap_items_count)
print("Amount of normal items bought", normal_items_count)
print("Amount of expensive items bought", expensive_items_count)
print("Total items bought:", items_total)
