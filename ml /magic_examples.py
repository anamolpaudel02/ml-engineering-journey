from ucimlrepo import fetch_ucirepo
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

columns = ["fLength", "fWidth", "fSize", "fConc", "fConc1", "fAsym", "fM3Long", "fM3Trans", "fAlpha", "fDist", "class"]
df = pd.read_csv("magic04.data", names = columns)

# for  class its g and h g for gammas and h for handrons
# since computer understand better i binary i.e 0 and 1 we will convert tha g and h to 0 and 1


df["class"] = (df["class"] == "g").astype(int)
# we donot need which one to be 0 or 1 we only ned 0 and 1 , here gamma is 1
print(df["class"].unique())

# Plot histograms of each feature for gamma-ray events (class = 1)


label_style = dict(bins=5,
    edgecolor="black",
    alpha=0.8,
    density = True)

# note: columns[-1]  "class" (one column name)
#     columns[:-1]  all feature names except "class"
for labels in columns[:-1] :
    # this lines says filters the dataset to only those rows and selects the current feature column
    plt.hist(df[df["class"] == 1][labels],**label_style,label ='gamma',color="skyblue")
    plt.hist(df[df["class"] == 0][labels],**label_style,label ='hadron',color="pink")

    plt.title(f"Distribution of {labels} for Gamma and Hadron ")
    plt.xlabel(labels)
    plt.ylabel("Probability")
    plt.show()

print(df.head())


