# we will learn to load data from files using pandas library. Pandas provides various functions to read data from different file formats such as CSV, Excel, JSON, and more. In this tutorial, we will focus on reading data from CSV files.


import pandas as pd 

coffee_data = pd.read_csv("./warmup-data/coffee.csv")
# print(coffee_data.head(5)) # Display the first 5 rows of the DataFrame
# print("Coffee Data:\n", coffee_data)

# print("tail of Coffee Data:\n", coffee_data.tail(5)) # Display the last 5 rows of the DataFrame

# # for accessing random rows we can use sample() function with random_state parameter to ensure reproducibility of the random sample. The random_state parameter allows us to set a seed for the random number generator, ensuring that we get the same random sample each time we run the code.
# print("Random sample of Coffee Data:\n", coffee_data.sample(5, random_state=42)) # Display a random sample of 5 rows here we have used random_state=42 to ensure that we get the same random sample each time we run the code.

# # now we will use loc to access specific rows and columns from the DataFrame. The loc function allows us to select data based on labels, making it easy to retrieve specific information from the DataFrame.
# print("Accessing specific rows and columns using loc:\n", coffee_data.loc[0:, ['coffee', 'units']]) # Accessing rows and columns of 
# print(coffee_data.loc[ "monday" : "tuesday"]) # Accessing rows and columns of DataFrame using loc
# # now we will use iloc to access specific rows and columns from the DataFrame. The iloc function allows us to select data based on integer positions, making it easy to retrieve specific information from the DataFrame.
# print("Accessing specific rows and columns using iloc:\n", coffee_data.iloc[0:, [0, 1]]) # Accessing rows and columns of DataFrame using iloc



# # using index
# coffee_data.index = coffee_data['coffee'] # Set the index of the DataFrame to the 'coffee' column
# print("DataFrame with index set to 'coffee' column:\n", coffee_data) # Display the DataFrame with the updated index

# we can modify using loc

coffee_data.loc['monday', 'units'] = 10 # Modify the value in the 'units' column for the row with index 'monday'
print("Modified Coffee Data:\n", coffee_data) # Display the modified DataFrame



# we can use .at and .at[] to access a single value for a row/column label pair. The .at[] function is used to access a single value in the DataFrame based on the row and column labels, while the .iat[] function is used to access a single value based on the integer position of the row and column.
print("Accessing a single value using .at[]:\n", coffee_data.at['monday', 'units']) # Accessing a single value using .at[] function





# sorting the data using sort_values() function. The sort_values() function allows us to sort the DataFrame based on one or more columns, making it easy to organize and analyze the data.
print (coffee_data.sort_values(
    by=['units', 'coffee'],
    ascending=[False, True]
    )
)


# we can use filtering to filter the data based on specific conditions. Filtering allows us to select rows from the DataFrame that meet certain criteria, making it easy to focus on relevant data for analysis.
print(
    "Filtering data based on specific conditions:\n", 
    coffee_data[coffee_data['units'] > 5]
    ) # Filter the DataFrame to include only rows where the 'units' column is


# we can use groupby() function to group the data based on specific columns. The groupby() function allows us to group the DataFrame by one or more columns, making it easy to perform aggregate operations on the grouped data.
print("Grouping data based on specific columns:\n", coffee_data.groupby('coffee').sum())

# we dan use str.contains() function to filter the data based on specific string patterns. The str.contains() function allows us to filter the DataFrame based on whether a specific string pattern is present in a column, making it easy to focus on relevant data for analysis.
print("Filtering data based on specific string patterns:\n", coffee_data[coffee_data['coffee'].str.contains('Latte|Espresso', case=False)]) # Filter the DataFrame to include only rows where the 'coffee' column contains the string 'latte' or 'espresso'

#  in above case = false means that the search is case-insensitive, so it will match 'latte', 'Latte', 'LATTE', etc.


# now we will use to find coffee with exactly 5 characters using str.contains() function with regex pattern. The regex pattern '^.{5}$' matches any string that has exactly 5 characters, allowing us to filter the DataFrame based on the length of the strings in the 'coffee' column.

print("Filtering data to find coffee with exactly 5 characters:\n", coffee_data[coffee_data['coffee'].str.contains(r'^.{5}$', case=False)]) # Filter the DataFrame to include only rows where the 'coffee' column has exactly 5 characters


# other related functions are str.startswith() and str.endswith() which can be used to filter the data based on whether a string starts or ends with a specific pattern. The str.startswith() function allows us to filter the DataFrame based on whether a string in a column starts with a specific pattern, while the str.endswith() function allows us to filter the DataFrame based on whether a string in a column ends with a specific pattern.
print(
    "Filtering data to find coffee that starts with 'C':\n",
    coffee_data[
        coffee_data["coffee"].str.contains(r"^C", case=False, na=False)
    ]
)


# starting with vowel using str.contains() function with regex pattern. The regex pattern '^[aeiou]' matches any string that starts with a vowel (a, e, i, o, u), allowing us to filter the DataFrame based on the first character of the strings in the 'coffee' column.
print(
    "Filtering data to find coffee that starts with a vowel:\n",
    coffee_data[
        coffee_data["coffee"].str.contains(r"^[aeiou]", case=False, na=False)
    ]
)

# if we add regex = False then it will treat the pattern as a literal string and not as a regex pattern. This means that it will look for an exact match of the string "^[aeiou]" in the 'coffee' column, rather than looking for strings that start with a vowel.



# now we will use .isin() function to filter the data based on whether a string is in a specific list of values. The str.isin() function allows us to filter the DataFrame based on whether a string in a column is present in a list of values, making it easy to focus on relevant data for analysis.
print(
    "Filtering data to find coffee that is in a specific list of values:\n",
    coffee_data[
        coffee_data["coffee"].isin(["Latte", "Espresso"])
    ]
)


# lets find the coffee type containing two vowels 
print (
    "coffee containing two vowels\n",
    coffee_data[
        coffee_data['coffee'].str.contains(
     r'[^AEIOUaeiou]*[^AEIOUaeiou][^AEIOUaeiou][^AEIOUaeiou]*[^AEIOUaeiou][^AEIOUaeiou]*$',
     na=False
      )
        ]
)

# for multiple condition instead of using & & we can use .query() function 
print( 
    "List of coffee espresso and units greater than 20\n",
    coffee_data.query(
        'coffee == "Espresso" and units > 20'
        )
      )



print (
     "Coffee that have repeated :\n",
    coffee_data[
        coffee_data['coffee'].str.contains(
        r'(.)\1'
        )  
      ] 
 )



# now we will add another section of price  but the main problem is that the individual price cannot be putted
print(coffee_data.head())

coffee_data['price'] = 230

print(coffee_data.head())




# now we will use numpy and add prices in every coffee type differently 




