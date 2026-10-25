
import matplotlib.pyplot as plt
import numpy as np

# A histogram is used to visualize the distribution of numerical data.



marks = np.array([
    35, 40, 45, 48, 50, 52, 55, 58, 60, 62,
    65, 67, 70, 72, 75, 78, 80, 82, 85, 90
])

# parameters :
   # bins      = number of intervals or groups
   # color     = color of the bars
   # edgecolor = color of the border of each bar
   # alpha     = transparency (0 to 1)
   # density   = True to normalize the histogram

plt.hist(
    marks,
    bins=5,
    color="skyblue",
    edgecolor="black",
    alpha=0.8
)

plt.title("Distribution of Students' Marks", fontsize=18)
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.grid(axis="y", alpha=0.3)
plt.show()
