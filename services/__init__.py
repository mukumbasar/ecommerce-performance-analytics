from services.customer_service import generate_customers
from services.order_service import generate_orders
from services.product_service import generate_products
from services.return_service import generate_returns

__all__ = [
    "generate_customers",
    "generate_products",
    "generate_orders",
    "generate_returns",
]