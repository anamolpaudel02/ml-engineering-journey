import matplotlib.pyplot as plt
import numpy as np

# grid() : helps make plot easier to read to read by adding reference line 
#  we can customize wither we need axis in one axis or both
x = [1,2,3,4,5]
y = [5,10,15,20,25]
plt.grid(axis="x",
         linewidth =2,
         color = "lightgrey",
         linestyle="dashed",
         )


plt.plot(x,y)
plt.show()
