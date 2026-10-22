import pandas as pd

# Sales records from two days
monday = pd.DataFrame({
    'day': ['Monday', 'Monday'],
    'coffee': ['Espresso', 'Latte'],
    'units': [30, 20]
})

tuesday = pd.DataFrame({
    'day': ['Tuesday', 'Tuesday'],
    'coffee': ['Espresso', 'Latte'],
    'units': [15, 25]
})

# Product price lookup table
prices = pd.DataFrame({
    'coffee': ['Espresso', 'Latte', 'Cappuccino'],
    'price': [4, 5, 6]
})

# 1. CONCAT: stack daily records vertically
all_sales = pd.concat(
    [monday, tuesday],
    ignore_index=True
)

# 2. MERGE: attach prices to the matching coffee
sales_with_prices = pd.merge(
    all_sales,
    prices,
    on='coffee',
    how='left'
)

# 3. Calculate revenue for each record
sales_with_prices['revenue'] = (
    sales_with_prices['units'] * sales_with_prices['price']
)

print(sales_with_prices)

# 4. Calculate total revenue by coffee
summary = sales_with_prices.groupby('coffee')['revenue'].sum()

print("\nTotal revenue by coffee:")
print(summary)