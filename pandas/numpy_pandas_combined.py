import numpy as np 
import pandas as pd

coffee = pd.read_csv("./warmup-data/coffee.csv")
coffee['price'] = 230
coffee['new_price'] = np.where(coffee['coffee'] == 'Espresso',3.99,5.99)


print(coffee.head(10))


# we can drop rows or columns

# lets drop 0 index 

print(
    "removing the zeroth index\n",
    coffee.drop(0)
    )


# lets drop new_price
print("\n")

print(
    "removing the new column new_price\n",
    coffee.drop(columns=['new_price'])
    )


# we can totally drop the column in the main csv file by using inplace


print(
    "removing the new column new_price\n",
    coffee.drop(columns=['price'], inplace=True)
    )

#  lets copy the coffee in new variable

coffee_new = coffee.copy()


coffee_new['new_price'] = 50

print(
    "This is the orginal one , coffee :\n",
    coffee
    )

print(
    "\nThis is the copied one , coffee_new :\n",
    coffee_new)

coffee['Revenue'] = coffee['units']*coffee['new_price']

print(
    "The new lists of data\n",
    coffee.head(10)
)

# now we will rename the new_price of coffee to new price for it either we use equal   or   inplace 


coffee.rename(columns={'new_price':'price'},inplace=True)
# or
# coffee = coffee.remane(columns={'new_price':'price'})

print(coffee.head()) 


#  now we will create a new csv file from here names coffee_new
coffee_new.to_csv('./warmup-data/coffee_new.csv')


# we can use landa and custom functions

coffee['Sales type'] = coffee['units'].apply(
    lambda x: 'less sales' if x < 10
    else ('average sales' if x < 20 else 'large sales')
    )

print(
    "Now we will classify the units based on unit sales:\n",
    coffee
    
)


# now we will look for numm value handling


coffee.loc[[0,1],'units'] = np.nan
print(
    "The 0th ans 1st index withh null value for null b=value handling are: \n",
    coffee.head()
)

# we can fill the nan value with number n using .fillna(n) function

print(
    "We will fill the nan with 1000",
    coffee.fillna(1000)
    )

# now we will add nan with mean of units

print(
    "We can change nan with the mean value of overall unit solds:\n",
    coffee.fillna(coffee['units'].mean())
)




# We can also fill NaN values using interpolate() and 
# .interpolate() estimates missing values using surrounding numeric values.

# Create missing values between known values
coffee.loc[[0,1],'units'] = 15
coffee.loc[[3, 4], 'units'] = np.nan

# Apply linear interpolation to estimate the missing values
print(coffee['units'].interpolate())

# we cannot use interple in beginniig one coz pandas to fill leading missing values using the nearest known
# now we will learn .dropna(), .isna(), and .notna()

# .isna() checks whether a value is NaN
# it returns True if the value is missing, otherwise False

print(
    "Checking which values are NaN:\n",
    coffee.isna()
)

# we can check only the units column
print(
    "\nChecking NaN values in units:\n",
    coffee['units'].isna()
)

# .isna().sum() counts the number of NaN values in each column

print(
    "\nCounting NaN values in each column:\n",
    coffee.isna().sum()
)


# .notna() checks whether a value is NOT NaN
# it returns True if the value exists, otherwise False

print(
    "\nChecking which values are NOT NaN:\n",
    coffee.notna()
)

# we can filter rows where units is not NaN
# only rows with valid units values will be displayed

print(
    "\nRows where units is NOT NaN:\n",
    coffee[coffee['units'].notna()]
)


# .dropna() removes rows containing NaN values
# by default, it removes a row if ANY column contains NaN

print(
    "\nRemoving rows containing NaN:\n",
    coffee.dropna()
)

# we can remove rows with NaN only in the units column
# NaN values in other columns will not affect this operation

print(
    "\nRemoving rows where units is NaN:\n",
    coffee.dropna(subset=['units'])
)


# we can also remove columns containing NaN values
# axis=1 means columns; axis=0 means rows

print(
    "\nRemoving columns containing NaN:\n",
    coffee.dropna(axis=1)
)


# how='all' removes a row only when ALL its values are NaN

print(
    "\nRemoving rows when all values are NaN:\n",
    coffee.dropna(how='all')
)


# important:
# dropna() does not modify the original coffee DataFrame by default
# to modify it directly, we can use inplace=True

# coffee.dropna(inplace=True)


# #################################

# now we will learn aggregation using value_counts()

# value_counts() counts how many times each unique value appears
# here we will count how many times each coffee type appears

print(
    "\nCounting each type of coffee:\n",
    coffee['coffee'].value_counts()
)

# normalize=True gives the proportion of each value instead of the count

print(
    "\nProportion of each coffee type:\n",
    coffee['coffee'].value_counts(normalize=True)
)

# we can also count values in the day column

print(
    "\nCounting records for each day:\n",
    coffee['day'].value_counts()
)

# groupby() groups rows that share the same value
# here, rows with the same coffee type are grouped together
# .sum() calculates the total units sold for each coffee type

print(
    "\nTotal units sold for each coffee type:\n",
    coffee.groupby('coffee')['units'].sum()
)

# .mean() calculates the average units sold for each coffee type
# NaN values are excluded from the mean by default

print(
    "\nAverage units sold for each coffee type:\n",
    coffee.groupby('coffee')['units'].mean()
)

# we can group by both day and coffee
# this shows units sold for each coffee type on each day

print(
    "\nTotal units grouped by day and coffee:\n",
    coffee.groupby(['day', 'coffee'])['units'].sum()
)

# .agg() allows us to calculate multiple statistics at once
# here we calculate total, average, minimum, and maximum units

print(
    "\nMultiple statistics for each coffee type:\n",
    coffee.groupby('coffee')['units'].agg(
        ['sum', 'mean', 'min', 'max', 'count']
    )
)

# calculate multiple statistics for different columns
# units: total and average units sold
# new_price: average selling price

print(
    "\nAggregating multiple columns:\n",
    coffee.groupby('coffee').agg(
        total_units=('units', 'sum'),
        average_units=('units', 'mean'),
        average_price=('price', 'mean')
    )
)

# pivot_table() summarizes values using row and column categories
# index='day' creates rows for each day
# columns='coffee' creates a separate column for each coffee type
# values='units' specifies the data to summarize
# aggfunc='sum' adds the units for each combination

print(
    "\nPivot table of units sold:\n",
    coffee.pivot_table(
        index='day',
        columns='coffee',
        values='units',
        aggfunc='sum'
    )
)



print(
    "Mean of each day coffee sale:\n",
    coffee.groupby('day').agg(
        units_mean = ('units','mean'),
        total_unit_sales= ('units','sum'),
        total_sales = ('Revenue','sum'),
    )
)

# this can be done by following but there is one problem that the same header cannot be used twice 
# if we try to add two header more than one time then the latest one will overide the previos one
print(
    "Mean of each day coffee sale:\n",
    coffee.groupby('day').agg({
        'units':'mean',  
        # 'units' :'sum',  
        
        "price" : 'sum'
    }
    )
)


print(
    "\nMultiple statistics for day price:\n",
    coffee.groupby('day')['price'].agg(
        ['sum', 'mean', 'min', 'max', 'count']
    )
)


# now we will learn some advance python fucationality: shift(), rolling() ,rank(),cumsum()

#     first we will learn about the .shift() function

# shift function is used to compare the data ,here we will compare the revenue in compare to yesterday

coffee['yesterday_revenure'] = coffee['Revenue'].shift(1)
# this will give yesterday revenue
coffee['Pct_change'] = ((coffee['Revenue']-coffee['yesterday_revenure'])/coffee['Revenue'])*100


# now we will use rank()

coffee['sales_rank'] = coffee['Revenue'].rank(ascending=False)
# in above coding if we remove ascending=False then if there is same rank like 2 has same it will give 1.5 for both making mid but if we add ascending=False then there will be integer
coffee.sort_values(['sales_rank'],ascending=False).sample()

# here the sample(10) will look the revenue of 10 row

# the cumsum() funtion will give the total of all time 

# note be careful if we do coffee.cumsum then it will give of all mes like if the data is 12345 then it gives 1 12 123 1234 12345 

coffee['cumulative_revenue'] = coffee['Revenue'].cumsum()

# rolling funtion is used to get the common type operation for n times
# if we want revenue of coffee type like latte 

lattee = coffee[coffee['coffee'] == "Latte"].copy()

lattee['3days'] = lattee['units'].rolling(3).sum()

print(
    "The sales for looking the Latte revenue sum of the last 3 days by using  rolling() :\n",
    lattee
    )

print(
    "This is the use of advance pandas summary of all output like using hift(),rank(),cumsum():\n",
    coffee.head(10)
    )


