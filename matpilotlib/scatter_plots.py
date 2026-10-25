
import matplotlib.pyplot as plt
import numpy as np

# Scatter plots are used to visualize the relationship between two numerical variables.



hours = np.array([1, 2, 3, 4, 5, 6, 7, 8])
marks = np.array([35, 40, 50, 48, 60, 70, 75, 90])

# parameters :
    # x, y        = data for horizontal and vertical axes
    # color or c  = color of the points
    # s           = size of the points
    # marker      = shape of the points
    # alpha       = transparency (0 to 1)

plt.scatter(
    hours,
    marks,
    color="blue",
    s=100,
    marker="o",
    alpha=0.7
)

plt.title("Hours Studied vs Marks Obtained", fontsize=18)
plt.xlabel("Hours Studied")
plt.ylabel("Marks Obtained")
# for show or hide grid lines we use true or false 
plt.grid(True,
         axis="both",
         linestyle="--",
         alpha=0.5)

plt.show()
