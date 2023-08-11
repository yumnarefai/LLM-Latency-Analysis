import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Read the data from the CSV file
data = pd.read_csv('data_hist.csv')

# Extract the word size labels from the first row
word_sizes = data.columns.tolist()

# Remove the first row (byte size labels)
data = data.iloc[1:, :]

# Set up the figure and axes
fig, ax = plt.subplots()

# Create the histograms based on word size
for column in data.columns:
    values = data[column].dropna().astype(float)
    
    # Plot histogram
    
    # Plot distribution curve
    sns.kdeplot(values, ax=ax, label=f'{column}B ')

# Customize labels, title, and grid
plt.xlabel('Time(s)')
plt.ylabel('Density')
plt.title('Distribution Curve with Time(s) Based on Prompt Size (B)')
plt.grid(True)

# Add a legend
plt.legend()

# Show the plot
plt.show()
