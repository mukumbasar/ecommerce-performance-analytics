import uuid
import pandas as pd
from config import PRODUCTS


def generate_products() -> pd.DataFrame:
    """Generates product catalog from predefined config products.

    Returns:
        pd.DataFrame: DataFrame containing product fields such as ID, name,
            category, unit price, and unit cost.
    """
    return pd.DataFrame({
        "product_id": [f"PROD-{uuid.uuid4()}" for _ in PRODUCTS],
        "product_name": [item[0] for item in PRODUCTS],
        "category": [item[1] for item in PRODUCTS],
        "unit_price": [item[2] for item in PRODUCTS],
        "unit_cost": [item[3] for item in PRODUCTS],
    })