import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Read the data from the CSV file
data = pd.read_csv('latency_time_dataset.csv', header=None)
values = sorted(data[0])

# Create the histogram
sns.kdeplot(values, color='blue', label='Distribution Curve with Time(s)', linewidth=2, bw_method=0.1)  # Adjust bw_method as needed
plt.xlabel('Time(s)')
plt.ylabel('Density')
plt.title('Distribution Curve with Time(s)')
plt.grid(True)

# Display the plot
plt.show()
