import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset("iris")

print(df.head())

sns.set(style="whitegrid")

plt.figure(figsize=(8,5))
sns.scatterplot(
    data=df,
    x="species",
    y="petal_length",
    size="sepal_width",
    hue="species",
    sizes=(20, 200),
    alpha=0.7
)
plt.title("Bubble Plot: Species vs Petal Length")
plt.show()

plt.figure(figsize=(6,4))
sns.countplot(data=df, x="species", hue="species")
plt.title("Count of Each Species")
plt.show()

plt.figure(figsize=(7,5))
sns.boxplot(data=df, x="species", y="sepal_width")
plt.title("Box Plot: Species vs Sepal Width")
plt.show()

plt.figure(figsize=(7,5))
sns.swarmplot(data=df, x="species", y="sepal_width")
plt.title("Swarm Plot: Species vs Sepal Width")
plt.show()

sns.displot(df["sepal_width"], kde=True)
plt.title("Distribution of Sepal Width")
plt.show()

sns.jointplot(data=df, x="sepal_length", y="sepal_width", kind="scatter")
plt.show()

sns.pairplot(df, hue="species")
plt.show()