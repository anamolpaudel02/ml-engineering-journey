# # tuple = (1,2,3,4,5)
# # a,b, c, d, e = tuple
# # # print(a)


import numpy as np
# # a = np.array([1, 2, 3, 4, 5])
# # # print(a)

# # b = np.array([[1, 2, 3], [4, 5, 6]])
# # # print(b) 
# # # print(a.ndim)
# # # print(b.ndim)
# # # print(a.shape)
# # # print(b.shape)
# # # print(a.nbytes)


# # # # accessing elements of an array

# # # # get a specific element [r,c]
# # # print( b[1,2]) # 6


# # # get specific row
# # print(b[0,:]) # [1 2 3]

# # c=np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9],[10, 11, 12 ]]])

# # # print(c.ndim)
# # print(c[:,1,:]) # 6

# # #inicializing all zeros
# # d = np.zeros((2,3))
# # print(d)

# # #inicializing all ones
# # e = np.ones((2,3))
# # print(e)

# # ##inicializing all random numbers(n)
# # # np.full((matrix size), n )
# # f = np.full((2,3,3),99, dtype=np.float16)
# # print(f)


# # #for similar size of f
# # g=np.full_like(f,4)
# # h=np.full(f.shape, 4)
# # print(g)
# # print(h)

# # # inicializing all random numbers
# # i = np.random.rand(2,3,3)
# # print(i)

# # j=np.random.randint(1,10,(2,3,3))
# # print(j)

# # k=np.random.random_sample(f.shape)
# # print(k)
 

# # #  repeat the element
# # arr = np.array([[1, 2], [3, 4]])
# # l = np.repeat(arr, 3, axis=1)
# # print(l)

# # # for number between between 1 and 100 with size of 2x3
# # m= np.random.randint(1, 100, (2,3))
# # print(m)
# # n = m 
# # n[0,0] = 100
# # print(m) # m will also change because n is a reference to m

# # # to remove this reference we can use copy()
# # o = m.copy()
# # o[0,0] = 200
# # print(m) # m will not change because o is a copy of m


# # # for matrix multiplication we can use @ or np.dot() or np.matmul()  
# # p = np.array([[1, 2], [3, 4]])
# # q = np.array([[5, 6], [7, 8]])
# # r = p @ q
# # print(r)


# s= np.identity(3)
# print(s)

# # for inverse of a matrix we can use np.linalg.inv()
# t = np.linalg.inv(s)
# print(t)
# # for traversing a matrix we can use np.transpose() or .T
# u = np.transpose(s)
# print(u)

# # for matrix norm we can use np.linalg.norm()
# v = np.linalg.norm(s)
# print(v)

filedata = np.genfromtxt(
    "/Users/anamolpaudel/Downloads/python/data.txt",
    delimiter=","
)
print(filedata)


# import os
\
# print(os.getcwd())