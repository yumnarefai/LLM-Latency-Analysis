import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


data = pd.read_csv('prompt_size_with_model_and_time_dataset.csv')

unique_models = data['model'].unique()
print(unique_models)
# Plot for each models
for model in unique_models:
    model_data = data[data['model'] == model]
    plt.scatter(model_data['x'], model_data['y'], label=model)

# Add regression lines
sns.lmplot(x='x', y='y', data=data, hue='model', legend=False)

plt.xlabel('Prompt Size (B)')
plt.ylabel('Time (s)')
plt.title('Prompt Size VS Performance across LLMs')
plt.legend()
plt.tight_layout()
plt.show()
