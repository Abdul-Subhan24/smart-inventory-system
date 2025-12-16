"""
Offline sales analysis script.

This script is not part of the Flask API.
It demonstrates how inventory or sales data
can be analyzed using pandas and matplotlib.
"""

import pandas as pd
import matplotlib.pyplot as plt
import sqlite3


def analyze_sales():
    conn = sqlite3.connect("database.db")

    df = pd.read_sql_query(
        "SELECT name, price, quantity FROM products",
        conn
    )

    conn.close()

    if df.empty:
        print("No data available for analysis.")
        return

    df["total_value"] = df["price"] * df["quantity"]

    summary = df.groupby("name")["total_value"].sum()
    summary.plot(kind="bar", title="Inventory Value by Product")

    plt.xlabel("Product")
    plt.ylabel("Total Value")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    analyze_sales()
