import pandas as pd
import sqlite3

# Load processed CSV
df = pd.read_csv("ecommerce_sales_processed.csv")

# Create SQLite database (this will create a file)
conn = sqlite3.connect("ecommerce_project.db")

# Load dataframe into SQL table
df.to_sql("sales_data", conn, if_exists="replace", index=False)

print("Data loaded into SQLite successfully!")

conn.close()
