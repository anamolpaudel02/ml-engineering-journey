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


coffee_new['new_price'] = 5.67

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



