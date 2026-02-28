import pandas as pd

# Read raw data
df = pd.read_csv("ecommerce_sales_raw.csv")

# Remove null values (if any)
df = df.dropna()

# Create total_amount column
df["total_amount"] = df["quantity"] * df["price"]

# Convert order_date to datetime
df["order_date"] = pd.to_datetime(df["order_date"])

# Extract month for analytics
df["order_month"] = df["order_date"].dt.month

# Save processed file
df.to_csv("ecommerce_sales_processed.csv", index=False)

print("Data transformation completed successfully!")
