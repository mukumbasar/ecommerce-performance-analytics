import uuid
import numpy as np
import pandas as pd
from config import (
    END_DATE, 
    NUM_ORDERS, 
    ORDER_STATUSES, 
    PAYMENT_METHODS, 
    START_DATE
    )

def generate_orders(
    customer_ids: np.ndarray,
    product_ids: np.ndarray,
    num_orders: int = NUM_ORDERS,
) -> pd.DataFrame:
    """Generates order transaction fact table using existing customer and product IDs.

    Args:
        customer_ids (np.ndarray): Array of valid customer IDs to select from.
        product_ids (np.ndarray): Array of valid product IDs to select from.
        num_orders (int): Total number of order records to generate.
            Defaults to NUM_ORDERS.

    Returns:
        pd.DataFrame: DataFrame containing transactions sorted chronologically.
    """
    random_dates = pd.date_range(start=START_DATE, end=END_DATE, freq="h")

    orders = pd.DataFrame({
        "order_id": [f"ORD-{uuid.uuid4()}" for _ in range(num_orders)],
        "customer_id": np.random.choice(customer_ids, num_orders),
        "product_id": np.random.choice(product_ids, num_orders),
        "order_date": np.random.choice(random_dates, num_orders),
        "quantity": np.random.randint(1, 5, num_orders),
        "order_status": np.random.choice(ORDER_STATUSES, num_orders),
        "payment_method": np.random.choice(PAYMENT_METHODS, num_orders),
    })

    return orders.sort_values(by="order_date").reset_index(drop=True)