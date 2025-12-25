import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
expenses = [2000, 1800, 2200, 2100]

plt.bar(months, expenses)
plt.title("Monthly Expenses")
plt.xlabel("Month")
plt.ylabel("Money")
plt.show()
