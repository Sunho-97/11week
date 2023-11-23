import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(0)
data = np.random.randn(100, 2)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Descriptive Statistics: Mean and Median
for i, color in enumerate(['blue', 'green']):
    sns.barplot(x=['Mean', 'Median'], y=[np.mean(data[:, i]), np.median(data[:, i])], color=color, alpha=0.7, ax=axes[0, 0], label=f'Variable {i+1}')
axes[0, 0].legend()
axes[0, 0].set_title('Descriptive Statistics: Mean and Median')

# Correlation Heatmap
sns.heatmap(data=np.corrcoef(data.T), annot=True, ax=axes[0, 1], cmap='coolwarm')
axes[0, 1].set_title('Correlation Analysis')

# Histograms
for i, color in enumerate(['blue', 'green']):
    sns.histplot(data=data[:, i], bins=15, color=color, alpha=0.7, ax=axes[1, 0], label=f'Variable {i+1}')
axes[1, 0].legend()
axes[1, 0].set(xlabel='Values', ylabel='Frequency', title='Histogram of Variables')

# Scatter Plot
sns.scatterplot(x=data[:, 0], y=data[:, 1], alpha=0.7, ax=axes[1, 1])
axes[1, 1].set(xlabel='Variable 1', ylabel='Variable 2', title='Scatter Plot of Variable 1 vs Variable 2')

plt.tight_layout()
plt.show()
