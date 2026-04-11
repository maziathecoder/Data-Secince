import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": list(range(1, 13)),

    "Face Cream": [2500, 2630, 2140, 3400, 3600, 2760, 2980, 3700, 3540, 1990, 2340, 2900],
    "Face Wash": [1500, 1200, 1240, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760],
    "Toothpaste": [5200, 5100, 4550, 5870, 4560, 4890, 4780, 5860, 6100, 8300, 7300, 7400],
    "Bathing Soap": [9200, 6100, 9550, 8870, 7760, 7490, 8980, 9960, 8100, 10300, 13300, 14400],
    "Shampoo": [1200, 2100, 3550, 1870, 1560, 1890, 1780, 2860, 2100, 2300, 2400, 1800],
    "Moisturizer": [1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760],

    "Total Units": [21100, 18330, 22470, 22270, 20960, 21140, 29550, 36140, 23400, 26670, 41280, 30020],

    "Total Profit": [211000, 183300, 224700, 222700, 296000, 200140, 295500, 361400,
                     234000, 266700, 412800, 300200]
}

df = pd.DataFrame(data)

plt.figure(figsize=(10,5))

plt.plot(df["Month"],
         df["Total Profit"],
         linestyle=":",
         marker="o",
         color="black")

plt.title("Month-wise Profit")
plt.xlabel("Month")
plt.ylabel("Profit")

plt.grid(True)
plt.show()

plt.figure(figsize=(10,5))

products = ["Face Cream", "Face Wash", "Toothpaste", "Bathing Soap", "Shampoo", "Moisturizer"]

for product in products:
    plt.plot(df["Month"],
             df[product],
             marker="o",
             linewidth=3,
             label=product)

plt.title("Monthly Sales of All Products")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()

plt.grid(True)
plt.show()

plt.figure(figsize=(10,5))

plt.plot(df["Month"], df["Face Cream"], marker="o", label="Face Cream")
plt.plot(df["Month"], df["Face Wash"], marker="o", label="Face Wash")

plt.title("Face Cream vs Face Wash Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()

plt.grid(True)
plt.show()