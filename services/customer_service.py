import uuid
import numpy as np
import pandas as pd
from config import (
    CITIES,
    COUNTRIES,
    FIRST_NAMES,
    LAST_NAMES,
    POSTCODES,
    SEGMENTS,
    STREETS,
    NUM_CUSTOMERS,
)

def generate_customers(num_customers: int = NUM_CUSTOMERS) -> pd.DataFrame:
    """Generates synthetic customer records with UUID keys and random profiles.

    Args:
        num_customers (int): Total number of customer records to construct.

    Returns:
        pd.DataFrame: DataFrame containing generated customer attributes.
    """
    return pd.DataFrame({
        "customer_id": [f"CUST-{uuid.uuid4()}" for _ in range(num_customers)],
        "customer_name": [
            f"{np.random.choice(FIRST_NAMES)} {np.random.choice(LAST_NAMES)}"
            for _ in range(num_customers)
        ],
        "address": [
            (
                f"{np.random.choice(STREETS)} {np.random.randint(1, 100)}, "
                f"Apt {np.random.randint(1, 15)}{np.random.choice(['A', 'B', 'C', ''])}"
            )
            for _ in range(num_customers)
        ],
        "city": np.random.choice(CITIES, num_customers),
        "postcode": np.random.choice(POSTCODES, num_customers),
        "country": np.random.choice(COUNTRIES, num_customers),
        "segment": np.random.choice(SEGMENTS, num_customers),
    })