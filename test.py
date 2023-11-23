import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(0)
data = np.random.randn(100, 2)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Bar Plot
sns.barplot(x=['Mean', 'Median'], y=[np.mean(data[:, 0]), np.median(data[:, 0])], color='blue', alpha=0.7, ax=axes[0, 0], label='Variable 1')
sns.barplot(x=['Mean', 'Median'], y=[np.mean(data[:, 1]), np.median(data[:, 1])], color='green', alpha=0.7, ax=axes[0, 0], label='Variable 2')
axes[0, 0].legend()
axes[0, 0].set_title('Descriptive Statistics: Mean and Median')

# Correlation Heatmap
sns.heatmap(data=np.corrcoef(data.T), annot=True, ax=axes[0, 1], cmap='coolwarm')
axes[0, 1].set_title('Correlation Analysis')

# Histograms
sns.histplot(data=data[:, 0], bins=15, color='blue', alpha=0.7, ax=axes[1, 0], label='Variable 1')
sns.histplot(data=data[:, 1], bins=15, color='green', alpha=0.7, ax=axes[1, 0], label='Variable 2')
axes[1, 0].legend()
axes[1, 0].set_xlabel('Values')
axes[1, 0].set_ylabel('Frequency')
axes[1, 0].set_title('Histogram of Variables')

# Scatter Plot
sns.scatterplot(x=data[:, 0], y=data[:, 1], alpha=0.7, ax=axes[1, 1])
axes[1, 1].set_xlabel('Variable 1')
axes[1, 1].set_ylabel('Variable 2')
axes[1, 1].set_title('Scatter Plot of Variable 1 vs Variable 2')

plt.tight_layout()
plt.show()
