import uuid
import numpy as np
import pandas as pd
from config import RETURN_RATE, RETURN_REASONS, RETURN_STATUSES


def generate_returns(
    orders_df: pd.DataFrame,
    return_rate: float = RETURN_RATE,
) -> pd.DataFrame:
    """Generates synthetic return records strictly for completed orders.

    Args:
        orders_df (pd.DataFrame): Generated orders DataFrame.
        return_rate (float): Fraction of completed orders to mark as returned.

    Returns:
        pd.DataFrame: DataFrame containing return records with return_id,
            order_id, customer_id, return_date, reason, and status.
    """
    # Strict filter: only completed orders are eligible for return
    completed = orders_df[orders_df["order_status"] == "Completed"]
    count = int(len(completed) * return_rate)

    selected = completed.sample(n=count).reset_index(drop=True)
    days_to_add = pd.to_timedelta(np.random.randint(1, 15, count), unit="D")

    return pd.DataFrame({
        "return_id": [f"RET-{uuid.uuid4()}" for _ in range(count)],
        "order_id": selected["order_id"].values,
        "customer_id": selected["customer_id"].values,
        "return_date": selected["order_date"] + days_to_add,
        "reason": np.random.choice(RETURN_REASONS, count),
        "status": np.random.choice(RETURN_STATUSES, count),
    })