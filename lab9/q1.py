# Write a Python program to display a bar chart and a pie chart for student height data taken
# from your class. Use different color for each bar and take at least 20 students.


import matplotlib.pyplot as plt
import numpy as np

heights = [150, 160, 165, 170, 175, 155, 180, 162, 168, 172, 
           158, 167, 174, 169, 171, 159, 164, 177, 156, 163]

students = [f'Student {i+1}' for i in range(len(heights))]

# Bar Chart
plt.figure(figsize=(10, 5))
bar_colors = plt.cm.viridis(np.linspace(0, 1, len(heights)))  # Different colors for each bar
plt.bar(students, heights, color=bar_colors)
plt.xlabel('Students')
plt.ylabel('Height (cm)')
plt.title('Student Heights Bar Chart')
plt.xticks(rotation=45)
# plt.tight_layout()
plt.show()

# Pie Chart
plt.figure(figsize=(8, 8))
plt.pie(heights, labels=students, autopct='%1.1f%%', startangle=140)
plt.title('Student Heights Pie Chart')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
