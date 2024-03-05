import random
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# List of 10 tshirt brands
brands = [
    "Nike",
    "Adidas",
    "Puma",
    "Under Armour",
    "Reebok",
    "Gucci",
    "Supreme",
    "Off-White",
    "Balenciaga",
    "Louis Vuitton",
]

# Generate a list of 100 tshirt brands from the above list at random
random_brands_list = [random.choice(brands) for _ in range(100)]

# Generate a list of 100 tshirt sizes corresponding to each tshirt
# in random_brands_list
tshirt_sizes = [random.choice(["S", "M", "L", "XL"]) for _ in range(100)]

# Encode the sizes from letters to numbers 1, 2, 3, 4
size_encoding_1234 = [
    1 if size == "S" else 2 if size == "M" else 3 if size == "L" else 4
    for size in tshirt_sizes
]

# Encode the sizes from letters to numbers 1, 2, 4, 8
size_encoding_1248 = [
    1 if size == "S" else 2 if size == "M" else 4 if size == "L" else 8
    for size in tshirt_sizes
]

# Generate a list of 100 weights, with larger average weights
# for larger sizes
weights = []
for size in tshirt_sizes:
    if size == "S":
        weights.append(random.uniform(100, 150))  # Average weight for S
    elif size == "M":
        weights.append(random.uniform(150, 200))  # Average weight for M
    elif size == "L":
        weights.append(random.uniform(200, 250))  # Average weight for L
    else:  # XL
        weights.append(random.uniform(250, 300))  # Average weight for XL


# Create a DataFrame with size encodings and weights
data = pd.DataFrame(
    {"Size_Encoding_1234": size_encoding_1234, "Weights": weights}  #
)  #

corr = data.corr("pearson")
sns.scatterplot(data, x=data["Size_Encoding_1234"], y=data["Weights"])
plt.annotate(
    f"Pearson Correlation: {corr.iloc[0,1]:.2f}",
    xy=(0.05, 0.95),
    xycoords="axes fraction",
    fontsize=12,
)
corr = data.corr("spearman")
plt.annotate(
    f"Spearman Correlation: {corr.iloc[0,1]:.2f}",
    xy=(0.05, 0.85),
    xycoords="axes fraction",
    fontsize=12,
)
plt.title(
    """Pearson & Spearman Correlation between Size
          Encoding 1234 and Weights"""
)
plt.show()

# Create a DataFrame with size encodings and weights
data = pd.DataFrame(
    {"Size_Encoding_1248": size_encoding_1248, "Weights": weights}  #
)  #

corr = data.corr("pearson")
sns.scatterplot(data, x=data["Size_Encoding_1248"], y=data["Weights"])
plt.annotate(
    f"Pearson Correlation: {corr.iloc[0,1]:.2f}",
    xy=(0.05, 0.95),
    xycoords="axes fraction",
    fontsize=12,
)
corr = data.corr("spearman")
plt.annotate(
    f"Spearman Correlation: {corr.iloc[0,1]:.2f}",
    xy=(0.05, 0.85),
    xycoords="axes fraction",
    fontsize=12,
)
plt.title(
    """Pearson Correlation between Size Encoding 1248 and
          Weights"""
)
plt.show()

print("We notice a drop in Pearson correlation!")
print(
    """It shows that Spearman is better at measuring the correlation
    between an
ordinal feature like tshirt size and a continuous feature like weight."""
)
print(
    """Spearman works better because it is rank based.
      hus different encodings will result in the same correlation."""
)
