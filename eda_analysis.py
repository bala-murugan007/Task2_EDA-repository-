import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("products_dataset.csv")

print("=" * 50)
print("CODEALPHA TASK 2 - EXPLORATORY DATA ANALYSIS")
print("=" * 50)

print("\n1. FIRST 5 ROWS")
print(df.head())

print("\n2. DATASET SHAPE")
print("Rows and Columns:", df.shape)

print("\n3. COLUMN NAMES")
print(df.columns.tolist())

print("\n4. DATA TYPES")
print(df.dtypes)

print("\n5. DATASET INFORMATION")
df.info()

print("\n6. MISSING VALUES")
print(df.isnull().sum())

print("\n7. DUPLICATE ROWS")
print("Number of duplicate rows:", df.duplicated().sum())

# Convert Price into numeric format
df["Price_Numeric"] = (
    df["Price"]
    .astype(str)
    .str.replace("Â£", "", regex=False)
    .str.replace("£", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.strip()
    .astype(float)
)

print("\n8. STATISTICAL SUMMARY")
print(df["Price_Numeric"].describe())

print("\n9. AVERAGE PRICE")
print("Average Price: £", round(df["Price_Numeric"].mean(), 2))

print("\n10. HIGHEST PRICE")
print("Highest Price: £", df["Price_Numeric"].max())

print("\n11. LOWEST PRICE")
print("Lowest Price: £", df["Price_Numeric"].min())

print("\n12. RATING DISTRIBUTION")
print(df["Rating"].value_counts())

print("\n13. AVAILABILITY DISTRIBUTION")
print(df["Availability"].value_counts())


# -----------------------------
# CHART 1 - PRICE DISTRIBUTION
# -----------------------------
plt.figure(figsize=(8, 5))
plt.hist(df["Price_Numeric"], bins=10)
plt.title("Product Price Distribution")
plt.xlabel("Price (£)")
plt.ylabel("Number of Products")
plt.tight_layout()
plt.savefig("eda_charts/price_distribution.png")
plt.show()
plt.close()


# -----------------------------
# CHART 2 - RATING DISTRIBUTION
# -----------------------------
plt.figure(figsize=(8, 5))
sns.countplot(x="Rating", data=df)
plt.title("Product Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Products")
plt.tight_layout()
plt.savefig("eda_charts/rating_distribution.png")
plt.show()
plt.close()


# -----------------------------
# CHART 3 - AVAILABILITY
# -----------------------------
plt.figure(figsize=(8, 5))
sns.countplot(x="Availability", data=df)
plt.title("Product Availability")
plt.xlabel("Availability")
plt.ylabel("Number of Products")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("eda_charts/availability_distribution.png")
plt.show()
plt.close()


# -----------------------------
# CHART 4 - TOP 10 EXPENSIVE PRODUCTS
# -----------------------------
top_products = df.sort_values(
    by="Price_Numeric",
    ascending=False
).head(10)

plt.figure(figsize=(10, 6))
plt.barh(
    top_products["Product Name"],
    top_products["Price_Numeric"]
)
plt.title("Top 10 Most Expensive Products")
plt.xlabel("Price (£)")
plt.ylabel("Product")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("eda_charts/top_10_expensive_products.png")
plt.show()
plt.close()


print("\n" + "=" * 50)
print("EDA COMPLETED SUCCESSFULLY!")
print("All charts saved inside eda_charts folder.")
print("=" * 50)         