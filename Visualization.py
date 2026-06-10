import pandas as pd
import matplotlib.pyplot as plt

# Read dataset
df = pd.read_excel("Dataset for Data Analytics (4).xlsx")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Chart 1 - Total Sales by Product
product_sales = df.groupby("Product")["TotalPrice"].sum()

product_sales.plot(kind="bar")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.show()

# Chart 2 - Payment Method Distribution
df["PaymentMethod"].value_counts().plot(kind="bar")

plt.title("Payment Method Distribution")
plt.xlabel("Payment Method")
plt.ylabel("Count")
plt.show()

# Chart 3 - Monthly Sales Trend
df["Month"] = df["Date"].dt.month

monthly_sales = df.groupby("Month")["TotalPrice"].sum()

monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.show()

# Chart 4 - Quantity vs Total Price
plt.scatter(df["Quantity"], df["TotalPrice"])

plt.title("Quantity vs Total Price")
plt.xlabel("Quantity")
plt.ylabel("Total Price")
plt.show()

print("Data visualization completed successfully!")