import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Read the data from the CSV file
data = pd.read_csv('prompt_size_with_time_dataset.csv')

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
    ax.hist(values, bins=10, alpha=0.7, label=f'Size:{column}B')
    
    # Plot distribution curve ( can remove so we can only see the histogram)
    sns.kdeplot(values, ax=ax, label=f'{column}B ', linestyle='dashed')

# Customize labels, title, and grid
plt.xlabel('Time(s)')
plt.ylabel('Density')
plt.title('Histograms with Time(s) Based on Prompt Size (B)')
plt.grid(True)

# Add a legend
plt.legend()

# Show the plot
plt.show()
