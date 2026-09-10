# generate_data.py

import os
import uuid
import numpy as np
import pandas as pd

# Import source constants from config.py
from config import (
    FIRST_NAMES,
    LAST_NAMES,
    STREETS,
    CITIES,
    COUNTRIES,
    POSTCODES,
    SEGMENTS,
)

# Set a random seed for reproducibility
np.random.seed(42)

# Ensure the output directory exists
os.makedirs("data", exist_ok=True)

# Generate synthetic European customer data
customers = pd.DataFrame({
    "customer_id": [f"CUST-{uuid.uuid4()}" for _ in range(200)],
    "customer_name": [
        f"{np.random.choice(FIRST_NAMES)} "
        f"{np.random.choice(LAST_NAMES)}"
        for _ in range(200)
    ],
    "address": [
        (
            f"{np.random.choice(STREETS)} {np.random.randint(1, 100)}, "
            f"Apt {np.random.randint(1, 15)}"
            f"{np.random.choice(['A', 'B', 'C', ''])}"
        )
        for _ in range(200)
    ],
    "city": np.random.choice(CITIES, 200),
    "postcode": np.random.choice(POSTCODES, 200),
    "country": np.random.choice(COUNTRIES, 200),
    "segment": np.random.choice(SEGMENTS, 200),
})

# Export to CSV inside the data directory
customers.to_csv("data/customers.csv", index=False)