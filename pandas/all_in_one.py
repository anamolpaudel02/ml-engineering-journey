
import pandas as pd

df = pd.read_csv('./warmup-data/coffee.csv')


# 1. CONCAT: STACK ROWS 

# axis=0 stacks rows vertically; ignore_index=True resets row labels
all_sales = pd.concat([df, df], axis=0, ignore_index=True)

print("\nVertical Concatenation:\n", all_sales)


# 2. CONCAT: COMBINE COLUMNS 

# axis=1 places columns side by side, aligned by index
result = pd.concat([df, df[['units']].rename(columns={'units': 'units_copy'})], axis=1)

print("\nHorizontal Concatenation:\n", result)


# 3. CONCAT: DIFFERENT COLUMNS 

df1 = pd.DataFrame({'coffee': ['Espresso'], 'units': [30]})
df2 = pd.DataFrame({'coffee': ['Latte'], 'price': [5]})

# Default join='outer' keeps all columns; missing values become NaN
result = pd.concat([df1, df2], ignore_index=True)

# join='inner' keeps only columns shared by both DataFrames
common_columns = pd.concat([df1, df2], ignore_index=True, join='inner')

print("\nDifferent Columns:\n", result)
print("\nCommon Columns Only:\n", common_columns)


# 4. MERGE: MATCH COMMON COLUMNS 

prices = pd.DataFrame({
    'coffee': ['Espresso', 'Cappuccino', 'Latte', 'Mocha'],
    'price': [4, 5, 6, 7]
})

# on='coffee' matches rows using the common coffee column
# how='inner' keeps only matching coffee names
inner = pd.merge(df, prices, on='coffee', how='inner')

print("\nInner Join:\n", inner)


# 5. TYPES OF MERGE JOINS 

# Keep all rows from the left DataFrame (df)
left = pd.merge(df, prices, on='coffee', how='left')

# Keep all rows from the right DataFrame (prices)
right = pd.merge(df, prices, on='coffee', how='right')

# Keep rows from both DataFrames; unmatched values become NaN
outer = pd.merge(df, prices, on='coffee', how='outer')

print("\nLeft Join:\n", left)
print("\nRight Join:\n", right)
print("\nOuter Join:\n", outer)


# 6. MERGE: DIFFERENT KEY NAMES 

prices_renamed = prices.rename(columns={'coffee': 'coffee_name'})

# left_on and right_on match columns with different names
result = pd.merge(
    df, prices_renamed,
    left_on='coffee',
    right_on='coffee_name',
    how='left'
)

print("\nDifferent Key Names:\n", result)


# 7. MERGE: OVERLAPPING COLUMN NAMES 

# Create updated data with a second 'units' column
updated = df.copy()
updated['units'] = updated['units'] + 5

# suffixes distinguish overlapping non-key columns
result = pd.merge(
    df, updated,
    on=['day', 'coffee'],
    suffixes=('_old', '_new')
)

print("\nOverlapping Columns:\n", result)


# 8. REAL APPLICATION: CALCULATE REVENUE 

# Add prices to sales, then calculate revenue
sales = pd.merge(df, prices, on='coffee', how='left')
sales['revenue'] = sales['units'] * sales['price']

print("\nSales Revenue:\n", sales)



# pd.concat([df1, df2])       -> Combine DataFrames
# axis=0                      -> Stack rows vertically
# axis=1                      -> Combine columns horizontally
# ignore_index=True           -> Reset row labels
# join='outer'                -> Keep all columns in concat
# join='inner'                -> Keep shared columns in concat
# on='coffee'                 -> Common column used to match rows
# how='inner'                 -> Keep matching keys only
# how='left'                  -> Keep all left-side rows
# how='right'                 -> Keep all right-side rows
# how='outer'                 -> Keep rows from both sides
# left_on / right_on          -> Match differently named columns
# suffixes=('_old', '_new')   -> Rename overlapping non-key columns
# NaN                         -> Missing value, often from no match
