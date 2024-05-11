# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# # Read data from CSV file  # Replace 'your_data.csv' with the path to your CSV file
# df = pd.read_csv('/Users/csuftitan/Documents/Election2024-main/data/tracking_data.csv')

# candidates = df['Candidate'].tolist()
# win_probabilities = df['Win Percentage'].tolist()
# date = df['Date'].tolist()
# Lb = df['LB'].tolist()
# Ub = df['UB'].tolist()

# # Create a range of colors using a colormap
# num_colors = len(candidates)
# colors = plt.cm.rainbow(np.linspace(0, 1, num_colors))

# # Plotting the bar chart
# plt.figure(figsize=(16, 10))
# x1 = [date]
# y1 = [win_probabilities]
# plt.plot(candidates, win_probabilities, color='blue')
# plt.plot(x1,y1, 'candidates')
# # Create the bar plot
# #plt.figure(figsize=(12, 8))
# #plt.bar(states, win_probabilities, color='blue')

# # Rotate x-axis labels for better readability
# plt.xticks(rotation=90)
# # Adding labels and title
# plt.xlabel("X-axis data")
# plt.ylabel("Y-axis data")
# plt.title('date')

# # Adding legend with the years
# plt.legend(candidates, win_probabilities, title='States')

# # Adding gridlines for better readability
# plt.grid(axis='y')

# # Rotating x-axis labels for better readability if needed
# plt.xticks(rotation=45)

# # Show plot
# plt.show()





# import pandas as pd
# import matplotlib.pyplot as plt

# # Data
# data = {
#     "Candidate": ["Trump", "Biden", "Trump", "Biden", "Trump", "Biden", "Trump", "Biden", "Trump", "Biden", "Trump"],
#     "Win Percentage": [0.21154, 0.7884599999999999, 0.1997, 0.8003, 0.2022, 0.7978000000000001, 0.21166, 0.78834, 0.2024, 0.7976, 0.19966],
#     "Date": ["2024-03-23", "2024-03-23", "2024-03-24", "2024-03-24", "2024-03-25", "2024-03-25", "2024-03-26", "2024-03-26", "2024-03-27", "2024-03-27", "2024-03-28"],
#     "LB": [0.13, 0.70692, 0.13, 0.7306, 0.12, 0.7156, 0.14, 0.7166800000000001, 0.13, 0.7252, 0.13],
#     "UB": [0.3, 0.8769199999999999, 0.2702499999999997, 0.8708499999999998, 0.28, 0.8756000000000002, 0.29, 0.86668, 0.28, 0.8752, 0.28]
# }

# # Create DataFrame
# df = pd.DataFrame(data)

# # Convert Date column to datetime
# df['Date'] = pd.to_datetime(df['Date'])

# # Plot line chart
# plt.figure(figsize=(10, 6))
# for candidate in df['Candidate'].unique():
#     candidate_data = df[df['Candidate'] == candidate]
#     plt.plot(candidate_data['Date'], candidate_data['Win Percentage'], marker='o', label=candidate)

# # Adding labels and title
# plt.xlabel('Date')
# plt.ylabel('Win Percentage')
# plt.title('Win Percentage Over Time')

# # Adding legend
# plt.legend()

# # Show plot
# plt.grid(True)
# plt.tight_layout()
# plt.show()



import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file into a pandas DataFrame
data = pd.read_csv('/Users/csuftitan/Documents/Election2024-main/data/tracking_data1.csv')

# Plotting
plt.figure(figsize=(10, 6))

# Plot win percentage for each candidate
for candidate in data['Candidate'].unique():
    candidate_data = data[data['Candidate'] == candidate]
    plt.plot(candidate_data['Date'], candidate_data['Win Percentage'], marker='o', linestyle='-', label=candidate)

# Set labels and title
plt.xlabel('Date')
plt.ylabel('Win Proportion')
plt.title('Winning Trend Over Time')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Add legend
plt.legend()

# Show plot
plt.grid(True)
plt.tight_layout()
plt.show()