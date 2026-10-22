import pandas as pd


# we will concate data: tsack rows vertically

monday = pd.DataFrame({
    'coffee': ['Espresso', 'Latte'],
    'units': [30, 20]
})

tuesday = pd.DataFrame({
    'coffee': ['Espresso', 'Latte'],
    'units': [15, 25]
})

# Add Tuesday's rows below Monday's rows
all_sales = pd.concat([monday, tuesday], axis=0, ignore_index=True)

print(all_sales)

# note:ignore_index=True resets the row labels to 0, 1, 2, 3. Without it, Pandas retains the original index labels, so duplicates can occur.


# we will concate data: place columns side by side 

coffee_names = pd.DataFrame({
    'coffee': ['Espresso', 'Latte', 'Mocha']
})

coffee_prices = pd.DataFrame({
    'price': [4, 5, 6]
})

# Add columns side by side, aligning by index
result = pd.concat([coffee_names, coffee_prices], axis=1)

print(result)

# Note :horizontal concatenation aligns rows by their index labels, not by matching the coffee names. If the indexes differ, the result may contain NaN values or more rows than expected.



# now wll will concate with diffenent columns


df1 = pd.DataFrame({
    'coffee': ['Espresso'],
    'units': [30]
})

df2 = pd.DataFrame({
    'coffee': ['Latte'],
    'price': [5]
})

# Stack rows and preserve all columns
result = pd.concat([df1, df2], ignore_index=True) 