
import numpy as np

# 1. Create a 3x3 array and extract its second row and last column
a1 = np.random.randint(1, 100, (3, 3))
print("Array:\n", a1)

second_row = a1[1, :]
last_column = a1[:, -1]

print("Second Row:", second_row)
print("Last Column:", last_column)


# 2. Generate 20 random numbers and calculate statistics
b1 = np.random.rand(20)

print("\nRandom Numbers:", b1)
print("Mean:", np.mean(b1))
print("Median:", np.median(b1))
print("Standard Deviation:", np.std(b1))
print("Minimum:", np.min(b1))
print("Maximum:", np.max(b1))


# 3. Reshape 12 numbers into a 3x4 matrix
c1 = np.arange(12).reshape(3, 4)
print("\nReshaped Matrix:\n", c1)


# 4. Calculate row-wise and column-wise sums
row_sums = np.sum(c1, axis=1)
column_sums = np.sum(c1, axis=0)

print("Row-wise Sums:", row_sums)
print("Column-wise Sums:", column_sums)


# 5. Filter an array to keep only values greater than 50
d1 = np.random.randint(1, 101, 20)
filtered = d1[d1 > 50]

print("\nOriginal Array:", d1)
print("Values greater than 50:", filtered)


# 6. Normalize an array using mean and standard deviation
e1 = (c1 - np.mean(c1)) / np.std(c1)
print("\nNormalized Matrix:\n", e1)


# 7. Multiply two compatible matrices using @
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

product = A @ B
print("\nMatrix Product:\n", product)


# 8. Demonstrate b = a versus b = a.copy()
a = np.array([1, 2, 3])

b = a
b[0] = 100
print("\nb = a")
print("a:", a)
print("b:", b)

a = np.array([1, 2, 3])

b = a.copy()
b[0] = 100
print("\nb = a.copy()")
print("a:", a)
print("b:", b)


before = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
after = before.reshape(2, 2, 3)
print("\nBefore Reshape:\n", before)
print("After Reshape:\n", after)



# we have some functions and rules for load sata from file and save data to file in numpy. 
# we can use np.loadtxt() for loading data from text file 
#  np.savetxt() for saving data to text file. 
# we can use np.load() for loading data from binary file 
# np.save() for saving data to binary file. 
# we can use np.genfromtxt() for loading data from text file with missing values. 
# we can use np.savez() for saving multiple arrays to a single binary file. 
# we can use np.savez_compressed() for saving multiple arrays to a single compressed binary file.