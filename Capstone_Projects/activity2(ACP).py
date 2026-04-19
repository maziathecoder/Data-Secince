import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("IMDB Dataset.csv")

print("First 3 rows:")
print(df.head(3))

print("\nLast 3 rows:")
print(df.tail(3))

print("\nDataset Info:")
print(df.info())

print("\nNull Values:")
print(df.isnull().sum())

subset = df.iloc[40:75]
print("\nSubset (rows 41 to 75):")
print(subset)

highest_votes = df.loc[df['Votes'].idxmax()]
print("\nMovie with highest votes:")
print(highest_votes)

plt.figure()
sns.boxplot(data=df[['IMDB_Rating', 'Runtime']])
plt.title("Box Plot of IMDb Rating and Runtime")
plt.show()

plt.figure()
plt.scatter(df['Runtime'], df['IMDB_Rating'])
plt.xlabel("Runtime")
plt.ylabel("IMDb Rating")
plt.title("Runtime vs IMDb Rating")
plt.show()

plt.figure()
sns.histplot(df['IMDB_Rating'], kde=True)
plt.title("Distribution of IMDb Rating")
plt.show()

plt.figure()
sns.histplot(df['Runtime'], kde=True)
plt.title("Distribution of Runtime")
plt.show()

plt.figure()
sns.countplot(x='Rating', data=df)
plt.xticks(rotation=45)
plt.title("Count of Movies by Rating")
plt.show()