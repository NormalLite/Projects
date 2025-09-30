import pandas as pd
import matplotlib.pyplot as plt
import os

"""
Sales Dashboard Project
- Reads sales data from CSV
- Summarizes total sales, sales by region and product
- Visualizes sales trends using line, bar, and pie charts
- Includes top product and region highlights
- Automatically creates a sample CSV if missing
"""

# Path to CSV
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "sales.csv")

# If CSV doesn't exist, create a sample one
if not os.path.exists(csv_path):
    print("CSV file not found. Creating sample sales.csv...")
    sample_data = {
        "Date": ["2025-09-01","2025-09-02","2025-09-03","2025-09-04","2025-09-05","2025-09-06"],
        "Region": ["North","South","East","West","North","South"],
        "Product": ["Product A","Product B","Product A","Product C","Product B","Product A"],
        "Sales": [500,700,450,600,550,650]
    }
    df = pd.DataFrame(sample_data)
    df.to_csv(csv_path, index=False)
    print("Sample CSV created successfully.")
else:
    df = pd.read_csv(csv_path)

# Summarize data
total_sales = df["Sales"].sum()
sales_by_region = df.groupby("Region")["Sales"].sum()
sales_by_product = df.groupby("Product")["Sales"].sum()
sales_over_time = df.groupby("Date")["Sales"].sum()
sales_cumulative = sales_over_time.cumsum()

# Top product and region
top_product = sales_by_product.idxmax()
top_region = sales_by_region.idxmax()

# Print summary
print("\n===== Sales Dashboard =====")
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Top Product: {top_product}")
print(f"Top Region: {top_region}\n")
print("Sales by Region:")
print(sales_by_region)
print("\nSales by Product:")
print(sales_by_product)

# Plotting
plt.figure(figsize=(16,6))

# 1. Sales over time
plt.subplot(1, 3, 1)
sales_over_time.plot(kind="line", marker="o")
sales_cumulative.plot(kind="line", marker="x", linestyle="--", color="red")
plt.title("Sales Over Time")
plt.ylabel("Sales ($)")
plt.xticks(rotation=45)
plt.legend(["Daily Sales", "Cumulative Sales"])

# 2. Sales by region
plt.subplot(1, 3, 2)
sales_by_region.plot(kind="bar", color="skyblue")
plt.title("Sales by Region")
plt.ylabel("Sales ($)")

# 3. Sales by product (bar + pie)
plt.subplot(1, 3, 3)
sales_by_product.plot(kind="bar", color="orange")
plt.title("Sales by Product")
plt.ylabel("Sales ($)")

plt.tight_layout()
plt.show()

# Optional: Pie chart for product sales
plt.figure(figsize=(6,6))
sales_by_product.plot(kind="pie", autopct="%1.1f%%", title="Sales by Product")
plt.ylabel("")
plt.show()
