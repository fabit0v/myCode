#!/usr/bin/env python3

import matplotlib.pyplot as plt

print("Would you like to place an order?")
choice = input("Type Y or N -->")

if choice.upper() == "Y":
    print("Great! Let's start your order.")


else:
    print("No? That's too bad...")


# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Cheese', 'Jalapenos', 'Mushroom', 'Sausage'
sizes = [30, 20, 20, 30]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.savefig("/home/student/static/myPizzaChart.png")

plt.show()
