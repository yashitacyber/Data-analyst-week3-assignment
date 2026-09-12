import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. CSV file ko load karna
df = pd.read_csv('data.csv')

print("--- Original Data ---")
print(df.head())

# 2. Missing values check karna aur handle karna
print("\n--- Missing Values Count ---")
print(df.isnull().sum())

# Missing values ko drop karna ya fill karna (jaise yahan drop kar rahe hain)
df = df.dropna()

# 3. Filtering rows (jaise jahan Duration 60 se zyada ho)
filtered_df = df[df['Duration'] >= 60]
print("\n--- Filtered Data (Duration >= 60) ---")
print(filtered_df.head())

# 4. Naya column create karna (jaise Calories aur Duration ka ratio)
df['Calories_Per_Minute'] = df['Calories'] / df['Duration']
print("\n--- Data with New Column ---")
print(df.head())

# 5. Basic Visualization (Matplotlib / Seaborn)
sns.histplot(df['Calories'], kde=True)
plt.title('Calories Distribution')
plt.xlabel('Calories')
plt.ylabel('Count')
plt.show()