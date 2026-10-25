import matplotlib.pyplot as plt
import numpy as np

# we can visualise the data using bar chart
categories = np.array(["Grains","Fruits","Vegetables","Protein","Dairy","Sweets"])

values = np.array([8,6,4,9,3,1])


plt.bar(categories,values)
plt.title("Consumption of different food",fontsize=25,
                                        family = "Arial",
                                        fontweight="bold",
                                          color = "pink")

plt.xlabel("Food")
plt.ylabel("in mgm")
plt.show()
