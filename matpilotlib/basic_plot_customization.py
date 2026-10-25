import matplotlib.pyplot as plt
import numpy as np
# plt.plot([1,2,3],[2,3,4])
# plt.show()

# better than normal one variable we use numpy because numpy is faster


x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15,25,30,20])
y2 = np.array([34,15,27,19])

# we can customize the plot i.e plot customization

# marker parameter 
    # marker = "." then it shows point in the coordinate and similar to *,o and many more
    # size: customize the size of marker by using markersize = or ms=
    # color of face :mfc or  markerfacecolor= , we can use rgb ,hexadecimal values or even coor
    # color of edge: markeredgecolor = mec for edge color and which is same as mfc
    # for line:
        # line style: linestyle="" (default is solid)  like dotted , dashed , dashedot, for no linr its none
        # line width: linewidth= line 1,2,3,4,5
        # line color: color = ""
# plt.plot( x,y1, marker = "o", 
#                markersize=10,
#                markerfacecolor="#30bcdc",
#                markeredgecolor= "#e9f2f4",
#                linestyle = "dotted",
#                linewidth = 2,
#                color = "#000D10"
#                )
# plt.plot( x,y2, marker = "o", 
#                markersize=10,
#                markerfacecolor="#30bcdc",
#                markeredgecolor= "#e9f2f4",
#                linestyle = "dotted",
#                linewidth = 2,
#                color = "#000D10"
#                )


# note : instead of rewriting them time and again we could build an dictatonary of it

# line_style = dict(marker = "o", 
#                markersize=10,
#                markerfacecolor="#30bcdc",
#                markeredgecolor= "#e9f2f4",
#                linestyle = "dotted",
#                linewidth = 2,
#                color = "#000D10"
#                 )

# for using them we need to unpack them using **
# plt.plot(x,y1, **line_style)
# plt.plot(x,y2, **line_style)


# if we need any marker character to be different just remove from the library and add on the plt

# we will now change the color of lines 
line_style = dict(marker = "o", 
               markersize=10,
               markerfacecolor="#30bcdc",
               markeredgecolor= "#e9f2f4",
               linestyle = "dotted",
               linewidth = 2
                )

plt.plot(x,y1, **line_style,color = "#060707")
plt.plot(x,y2, **line_style,color = "#10C6EF")



# Lables

# to give tite  we use :title() function 

# title customization:
    # for font size we use:fontsize = 
    # font style we use : family =
    # for type or weight we use: fontweight=
    # for color we just:use color=
plt.title("Class size", fontsize=25,
                         family = "Arial",
                         fontweight="bold",
                         color = "#10C6EF")

label_style = dict(fontsize=15,
                 family = "Arial",
                 fontweight="bold",
                color = "#89A7AE")

# for the lables in two coordinate in 2d we use xlabel and ylabel for respective x and y coordinate

plt.xlabel("Year",**label_style)
plt.ylabel("Student",**label_style)
# for the axis coordinate we use ticks_params

plt.tick_params(axis="both",
                colors="#89A7AE")
# We can see that the grap in x axis are 2023.0,2023.5 and so on but we need 2023,2024 and so on for that we use ticks() function
plt.xticks(x)






plt.show()