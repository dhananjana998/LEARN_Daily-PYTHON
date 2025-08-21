import numpy as np


    # shop items
    items = ["Bread", "Pizza", "Cake", "Burger"]
    # item price
    prices = np.array([160, 1250, 500, 750])
    sales = []

    for d in range(1, 8):
        print(f"Day {d}:")
        day_sales = [int(input(f"   {item}: ")) for item in items]
        sales.append(day_sales)

    sales = np.array(sales)

    # calculation
    total_item = np.sum(sales, axis=0)
    total_per_item_cost = total_item * prices

    print("\n------------------------ Shop Summary ------------------------")
    print("Total sold per item:", dict(zip(items, total_item)))
    print("Total per items cost:", dict(zip(items, total_per_item_cost)))



