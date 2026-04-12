import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Tips Dataset.csv")

print(df.head())

print(df[['total_bill', 'tip', 'size']].describe())

sns.set(style="whitegrid")

plt.figure()
sns.histplot(df['total_bill'], kde=True)
plt.title("Distribution of Total Bill")
plt.xlabel("Total Bill")
plt.ylabel("Frequency")
plt.show()

plt.figure()
sns.scatterplot(x='total_bill', y='tip', hue='time', data=df)
plt.title("Total Bill vs Tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.show()

sns.pairplot(df, hue='gender')
plt.show()