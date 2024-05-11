import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# # Read data from CSV file  # Replace 'your_data.csv' with the path to your CSV file
# df = pd.read_csv('/Users/csuftitan/Documents/Election2024-main/data/simulation_data.csv')

# winners = df['winner'].tolist()
# points = df['points'].tolist()
# # values = df['n'].tolist()

# # Create a range of colors using a colormap
# num_colors = len(winners)
# colors = plt.cm.rainbow(np.linspace(0, 1, num_colors))

# # Plotting the bar chart
# plt.figure(figsize=(10, 6))
# bars = plt.bar(winners, points, color=colors)

# # Adding labels and title
# plt.xlabel('Winners')
# plt.ylabel('points')
# plt.title('Wins')

# # Adding legend with the years
# plt.legend(bars, winners, title='winner')

# # Adding gridlines for better readability
# plt.grid(axis='y')

# # Rotating x-axis labels for better readability if needed
# plt.xticks(rotation=45)

# # Show plot
# plt.show()

# # This is the code I used

import matplotlib.pyplot as plt

# Load data from CSV file into a pandas DataFrame
data = pd.read_csv('/Users/csuftitan/Documents/Election2024-main/data/simulation_data.csv')

# Plotting
plt.figure(figsize=(10, 6))

# Create a bar plot
plt.bar(data['winner'], data['points'], color='blue')

# Add labels and title
plt.xlabel('Winner')
plt.ylabel('Points')
plt.title('Winner by Points')

# Show plot
plt.tight_layout()
plt.show()