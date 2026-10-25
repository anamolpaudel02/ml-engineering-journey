import matplotlib.pyplot as plt
import numpy as np

# bar chart is circular chart divided into different elements in 360 degree 

# this is good for visualizing distribution among the different element or categories

# some impotant parameters of piechart

    # for showing auto percentage we use autopct="%x.xxf%%" for 2 digit after decimal
    # for labels we use labels = ....
    # for displace slightly from the orginal one we use explode =[] :: better to use between 0-1
    #  for shadow to be show we use shadow= true and for not false
    # for changing angle accordingly to us of pie chart er use straightangle = angle
# we will try to create the pie chart among the number of student in different faculties of engineering student of any uni lets say wrc

faculties = ["Computer","Civil","Electronic","Electrical","Mechanical","Geomatric"]
colors = ["red","yellow","blue","green","violet","grey"]
students=[46,116,45,47,34,23]

plt.pie(students,labels=faculties,
                autopct="%1.1f%%",
                colors=colors,
                explode =[0,0,0,0.1,0,0.1],
                shadow=True,
                startangle=90
                )

plt.title("No of students in different Faculties")


plt.show()