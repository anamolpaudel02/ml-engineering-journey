from pathlib import Path
import numpy as np

filedata = np.genfromtxt("data.txt", delimiter=",")
print("Data from file:\n", filedata)

# indexing can be done using boolean indexing, where we can use a condition to filter the data.


a = filedata[filedata > 50]
print("Values greater than 50:", a)
# for specific indices we can use filedata[[row_indices],[column_indices]] to get the values at those indices.
print("Values at indices 2*3 and 3*2 form matrix:", filedata[[1,2],[2,1]])

print("Values at indices [1,2]:", filedata[[1,2]])
print("value at index 0 and 1 of a is",a[0],a[1])

# in filedata array for filedata[1] selects second row and filedata[:,1] selects second column.
# for individual element we can use filedata[1,2] which selects the element at second row and third column.



c=np.any(filedata>50,axis=0)
print("Any value greater than 50:", c)
print(np.any(filedata>50,axis=0))

d=np.all(filedata>50,axis=0)
print("All values greater than 50:", d)
print(np.all(filedata>50,axis=0))