import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read data from CSV file  # Replace 'your_data.csv' with the path to your CSV file
df = pd.read_csv('/Users/csuftitan/Documents/Election2024-main/data/state_probabilities.csv')

states = df['State'].tolist()
win_probabilities = df['Trump Win Prob.'].tolist()
# values = df['n'].tolist()


# Create a range of colors using a colormap
num_colors = len(states)
colors = plt.cm.rainbow(np.linspace(0, 1, num_colors))

# Plotting the bar chart
plt.figure(figsize=(12, 8))
bars = plt.bar(states, win_probabilities, color=colors)
# Create the bar plot
#plt.figure(figsize=(12, 8))
#plt.bar(states, win_probabilities, color='blue')

# Rotate x-axis labels for better readability
plt.xticks(rotation=90)
# Adding labels and title
plt.xlabel('States')
plt.ylabel('Win Proabability')
plt.title('Trumps Win Probability State-wise')

# Adding legend with the years
plt.legend(states, win_probabilities, title='States')

# Adding gridlines for better readability
plt.grid(axis='y')

# Rotating x-axis labels for better readability if needed
plt.xticks(rotation=45)

# Show plot
plt.show()

