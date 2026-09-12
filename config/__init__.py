from config.customer_config import (
    CITIES,
    COUNTRIES,
    FIRST_NAMES,
    LAST_NAMES,
    POSTCODES,
    SEGMENTS,
    STREETS,
    NUM_CUSTOMERS,
)
from config.order_config import (
    END_DATE,
    NUM_ORDERS,
    ORDER_STATUSES,
    PAYMENT_METHODS,
    START_DATE,
)
from config.product_config import PRODUCTS
from config.return_config import RETURN_RATE, RETURN_REASONS, RETURN_STATUSES

__all__ = [
    "FIRST_NAMES",
    "LAST_NAMES",
    "STREETS",
    "CITIES",
    "COUNTRIES",
    "POSTCODES",
    "SEGMENTS",
    "PRODUCTS",
    "NUM_ORDERS",
    "ORDER_STATUSES",
    "PAYMENT_METHODS",
    "START_DATE",
    "END_DATE",
    "RETURN_RATE",
    "RETURN_REASONS",
    "RETURN_STATUSES",
]