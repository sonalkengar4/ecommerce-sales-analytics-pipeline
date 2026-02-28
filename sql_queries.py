import sqlite3
import pandas as pd

conn = sqlite3.connect("ecommerce_project.db")

queries = {
    "Total Revenue": """
        SELECT SUM(total_amount) AS total_revenue
        FROM sales_data;
    """,

    "Revenue by Category": """
        SELECT category, SUM(total_amount) AS revenue
        FROM sales_data
        GROUP BY category
        ORDER BY revenue DESC;
    """,

    "Revenue by City": """
        SELECT city, SUM(total_amount) AS revenue
        FROM sales_data
        GROUP BY city
        ORDER BY revenue DESC;
    """,

    "Monthly Revenue": """
        SELECT order_month, SUM(total_amount) AS revenue
        FROM sales_data
        GROUP BY order_month
        ORDER BY order_month;
    """,

    "Payment Method Usage": """
        SELECT payment_type, COUNT(*) AS transactions
        FROM sales_data
        GROUP BY payment_type
        ORDER BY transactions DESC;
    """
}

for title, query in queries.items():
    print(f"\n--- {title} ---")
    result = pd.read_sql_query(query, conn)
    print(result)

conn.close()
