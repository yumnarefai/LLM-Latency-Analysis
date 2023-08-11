
# import matplotlib.pyplot as plt
# import pandas as pd

# # Read the data from the CSV file
# data = pd.read_csv('data_hist.csv', header=None)
# values = data[0]

# # Define the discrete variables
# discrete_variables = [424, 494, 564, 662, 774]

# # Create separate histograms for each discrete variable
# for variable in discrete_variables:
#     subset_values = values[data[0] == variable]
    
#     plt.hist(subset_values, bins=15, alpha=0.6, edgecolor='black', label=f'Discrete Variable {variable}')
    
# plt.xlabel('Values')
# plt.ylabel('Frequency')
# plt.title('Histograms for Discrete Variables')
# plt.grid(True)
# plt.legend()

# # Display the plot
# plt.show()
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Read the data from the CSV file
data = pd.read_csv('latency_time_dataset.csv')

# Set up the figure and axes
fig, ax = plt.subplots()

# Create the histograms based on word size

    # Plot histogram
ax.hist(data, bins=10, alpha=0.7, color='blue' )
    
    # Plot distribution curve

# Customize labels, title, and grid
plt.xlabel('Time(s)')
plt.ylabel('Density')
plt.title('Histogram Distribution with Time(s)')
plt.grid(True)

# Add a legend
plt.legend()

# Show the plot
plt.show()
