# Install these before running:
# pip install pandas matplotlib

import pandas as pd
import matplotlib.pyplot as plt

# ====== Step 1: Simulate Data Collection ======
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [12000, 15000, 17000, 13000, 16000, 18000],
    "Costs": [8000, 9000, 9500, 8500, 9000, 10000]
}

df = pd.DataFrame(data)

# ====== Step 2: Data Processing & Insights ======
df["Profit"] = df["Sales"] - df["Costs"]
avg_sales = df["Sales"].mean()
best_month = df.loc[df["Profit"].idxmax(), "Month"]

print("=== Business Insights ===")
print(f"Average Monthly Sales: ₹{avg_sales:,.2f}")
print(f"Best Month by Profit: {best_month}")
print("\nSales and Profit Data:\n", df)

# ====== Step 3: Visualization ======
plt.figure(figsize=(8,6))
plt.plot(df["Month"], df["Sales"], marker='o', label="Sales")
plt.plot(df["Month"], df["Profit"], marker='o', label="Profit")
plt.title("Sales & Profit Trend")
plt.xlabel("Month")
plt.ylabel("Amount (₹)")
plt.legend()
plt.grid(True)
plt.show()
