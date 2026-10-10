import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("ecommerce_sales_data.csv")

# Convert date
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)

# Calculate total sales
df["Total Sales"] = df["Quantity"] * df["Price"]

# ---------------- BASIC ANALYSIS ----------------

print("\n========== E-COMMERCE SALES ANALYSIS ==========")

print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nStatistical Summary:")
print(df.describe())

# Total revenue
total_revenue = df["Total Sales"].sum()
print("\nTotal Revenue:", round(total_revenue, 2))

# Total quantity
total_quantity = df["Quantity"].sum()
print("Total Quantity Sold:", total_quantity)

# Average order value
average_order_value = df["Total Sales"].mean()
print("Average Order Value:", round(average_order_value, 2))

# ---------------- CATEGORY ANALYSIS ----------------

category_sales = df.groupby("Product Category")["Total Sales"].sum().sort_values(ascending=False)

print("\nSales by Product Category:")
print(category_sales)

# ---------------- PRODUCT ANALYSIS ----------------

product_sales = df.groupby("Product Name")["Total Sales"].sum().sort_values(ascending=False)

print("\nTop Products:")
print(product_sales.head(10))

# ---------------- CITY ANALYSIS ----------------

city_sales = df.groupby("City")["Total Sales"].sum().sort_values(ascending=False)

print("\nSales by City:")
print(city_sales)

# ---------------- PAYMENT METHOD ----------------

payment_sales = df.groupby("Payment Method")["Total Sales"].sum().sort_values(ascending=False)

print("\nSales by Payment Method:")
print(payment_sales)

# ---------------- MONTHLY SALES ----------------

df["Month"] = df["Order Date"].dt.to_period("M").astype(str)

monthly_sales = df.groupby("Month")["Total Sales"].sum()

print("\nMonthly Sales:")
print(monthly_sales)

# ---------------- SAVE ANALYSIS ----------------

df.to_csv("ecommerce_sales_analysis.csv", index=False)

print("\nAnalysis file saved as ecommerce_sales_analysis.csv")

# ---------------- CHART 1 ----------------

plt.figure(figsize=(8,5))
category_sales.plot(kind="bar")
plt.title("Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("sales_by_category.png")
plt.close()

# ---------------- CHART 2 ----------------

plt.figure(figsize=(8,5))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_sales_trend.png")
plt.close()

# ---------------- CHART 3 ----------------

plt.figure(figsize=(8,5))
city_sales.plot(kind="bar")
plt.title("Sales by City")
plt.xlabel("City")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("sales_by_city.png")
plt.close()

print("\nCharts created successfully!")
print("1. sales_by_category.png")
print("2. monthly_sales_trend.png")
print("3. sales_by_city.png")

print("\n========== ANALYSIS COMPLETED ==========")