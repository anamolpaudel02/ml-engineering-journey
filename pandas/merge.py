
import pandas as pd

# Original sales data
sales = pd.DataFrame({
    'day': ['monday', 'tuesday', 'wednesday'],
    'coffee': ['Espresso', 'Cappuccino', 'Latte'],
    'units': [30, 34, 25],
    'price': [3.99, 5.99, 5.99]
})

# Updated sales data (Mocha is a new coffee)
sales_update = pd.DataFrame({
    'coffee': ['Espresso', 'Cappuccino', 'Latte', 'Mocha'],
    'units': [32, 36, 28, 10],
    'price': [4.49, 6.49, 6.49, 5.49]
})

# INNER: only matching coffees
inner = pd.merge(sales, sales_update, on='coffee',
                 how='inner', suffixes=('_old', '_new'))

# LEFT: keep all original sales
left = pd.merge(sales, sales_update, on='coffee',
                how='left', suffixes=('_old', '_new'))

# RIGHT: keep all updated sales
right = pd.merge(sales, sales_update, on='coffee',
                 how='right', suffixes=('_old', '_new'))

# OUTER: keep coffees from both DataFrames
outer = pd.merge(sales, sales_update, on='coffee',
                 how='outer', suffixes=('_old', '_new'))

# Display results
print("INNER MERGE:\n", inner)
print("\nLEFT MERGE:\n", left)
print("\nRIGHT MERGE:\n", right)
print("\nOUTER MERGE:\n", outer)



# here
# on='coffee'  # Common column used to match rows

# how='inner'  # Keep only matching rows

# how='left'   # Keep all rows from the left DataFrame

# how='right'  # Keep all rows from the right DataFrame

# how='outer'  # Keep rows from both DataFrames

# suffixes=('_old', '_new')  # Rename overlapping columns to distinguish their sources