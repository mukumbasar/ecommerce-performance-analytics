# generate_data.py

import os
import numpy as np
from services import (
    generate_customers,
    generate_orders,
    generate_products,
    generate_returns,  # <-- Added
)

np.random.seed(42)
os.makedirs("data", exist_ok=True)

if __name__ == "__main__":
    print("\nGenerating synthetic datasets...\n")

    # 1. Customers
    customers_df = generate_customers()
    customers_df.to_csv("data/customers.csv", mode="w", index=False)
    print(f"Generated {len(customers_df)} customers -> data/customers.csv")

    # 2. Products
    products_df = generate_products()
    products_df.to_csv("data/products.csv", mode="w", index=False)
    print(f"Generated {len(products_df)} products -> data/products.csv")

    # 3. Orders
    orders_df = generate_orders(
        customer_ids=customers_df["customer_id"].values,
        product_ids=products_df["product_id"].values,
    )
    orders_df.to_csv("data/orders.csv", mode="w", index=False)
    print(f"Generated {len(orders_df)} orders -> data/orders.csv")

    # 4. Returns
    returns_df = generate_returns(orders_df)
    returns_df.to_csv("data/returns.csv", mode="w", index=False)
    print(f"Generated {len(returns_df)} returns -> data/returns.csv")

    print("\nAll datasets successfully created in data\n")