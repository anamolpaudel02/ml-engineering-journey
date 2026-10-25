
import matplotlib.pyplot as plt
import numpy as np

# Subplots allow us to display multiple charts inside a single figure


hours = np.array([1, 2, 3, 4, 5, 6, 7, 8])
marks = np.array([35, 40, 50, 48, 60, 70, 75, 90])

#  parameters:
    # nrows = number of rows of subplots
    # ncols = number of columns of subplots
    # figsize = overall figure size
    
# ax      = individual subplot axes

fig, ax = plt.subplots(
    nrows=1,
    ncols=2,
    figsize=(12, 5)
)

# First subplot: scatter plot
ax[0].scatter(hours, marks, color="blue", s=80)

ax[0].set_title("Hours vs Marks")
ax[0].set_xlabel("Hours Studied")
ax[0].set_ylabel("Marks")

# Second subplot: histogram
ax[1].hist(
    marks,
    bins=5,
    color="orange",
    edgecolor="black"
)

ax[1].set_title("Distribution of Marks")
ax[1].set_xlabel("Marks")
ax[1].set_ylabel("Frequency")

# Adjust spacing between subplots
plt.tight_layout()

plt.show()
