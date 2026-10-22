import pandas as pd

df=pd.DataFrame({
    'A':[1,2,3,4],
    'B':[5,6,7,8],
    'C':[9,10,11,12]    
})


df2 = pd.DataFrame(
    [
        [1, 2, 3, 4],
        [4, 5, 6, 7],
        [8, 9, 10, 11],
        [12, 13, 14, 15]
    ],
    columns=['A', 'B', 'C', 'D']
)

print(df2)

print("DataFrame:\n",df)
print("DataFrame2:\n",df2)

# we will look head

# we will look data till 2nd row
print("Head of DataFrame:\n",df.head(2)) 

# we will look data till 3rd row
print("Head of DataFrame2:\n",df2.head(3))


# we will look tail
print("Tail of DataFrame:\n",df.tail(2))


# we can access columns and rows using loc and iloc

print("Accessing column A using loc:\n",df.loc[:, 'A'])
print("Accessing column B using iloc:\n",df.iloc[:, 1])


# we can acces index and columns using loc and iloc
print("Accessing index 1 and column B using loc:\n",df.loc[1, 'B'])
print("Accessing index 2 and column C using iloc:\n",df.iloc[2, 2])

#  the main difference between loc and iloc is that loc is label based indexing and iloc is integer based indexing.

# info() function is used to get the information of the DataFrame.
print("Information of DataFrame:\n",df.info())


# for unique values we can use unique() function
print("Unique values in column A:\n",df['A'].unique())

# for shape of the DataFrame we can use shape attribute
print("Shape of DataFrame:\n",df.shape)


# describe() function is used to get the summary statistics of the DataFrame.
print("Summary statistics of DataFrame:\n",df.describe()) 

