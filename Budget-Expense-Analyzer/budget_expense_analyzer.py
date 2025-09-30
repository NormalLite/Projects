import pandas as pd
import matplotlib.pyplot as plt

"""
Interactive Budget vs Actual Expense Analyzer
- Users input budget per category
- Users input transactions (date, category, amount)
- Automatically sums spending per category
- Calculates variance and highlights overspending
- Generates bar and pie charts
"""

categories = ["Rent", "Food", "Transport", "Entertainment", "Other"]

budget = {}
print("Enter your planned budget for each category:")
for cat in categories:
    while True:
        try:
            value = float(input(f"{cat}: $"))
            if value < 0:
                raise ValueError
            budget[cat] = value
            break
        except ValueError:
            print("Please enter a valid positive number.")

transactions = []
print("\nEnter your expense transactions. Type 'done' when finished.")
while True:
    date = input("Date (YYYY-MM-DD) or 'done' to finish: ")
    if date.lower() == "done":
        break
    category = input(f"Category ({', '.join(categories)}): ")
    if category not in categories:
        print("Invalid category, try again.")
        continue
    try:
        amount = float(input("Amount ($): "))
        if amount < 0:
            raise ValueError
        transactions.append({"Date": date, "Category": category, "Amount": amount})
    except ValueError:
        print("Please enter a valid positive number.")

df_transactions = pd.DataFrame(transactions)

actual = df_transactions.groupby("Category")["Amount"].sum()
df_summary = pd.DataFrame({
    "Budget": pd.Series(budget),
    "Actual": actual
}).fillna(0)

df_summary["Variance"] = df_summary["Actual"] - df_summary["Budget"]

print("\n===== Budget vs Actual Report =====")
print(df_summary)

overspend = df_summary[df_summary["Variance"] > 0]
if not overspend.empty:
    print("\nCategories over budget:")
    print(overspend[["Variance"]])

plt.figure(figsize=(12,5))
df_summary[["Budget","Actual"]].plot(kind="bar", figsize=(12,5))
plt.title("Budget vs Actual Spending by Category")
plt.ylabel("Amount ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(6,6))
df_summary["Actual"].plot(kind="pie", autopct="%1.1f%%", title="Actual Spending by Category")
plt.ylabel("")
plt.show()

