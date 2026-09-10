# config.py

# Static customer references for synthetic data generation
FIRST_NAMES = [
    'Oliver', 'Emma', 'Lucas', 'Mia', 'Liam', 'Sofia', 'Matteo', 'Giulia',
    'Finn', 'Anna', 'Hugo', 'Camille', 'Lukas', 'Lina', 'Noah', 'Elena',
    'Antoine', 'Freja', 'Alejandro', 'Clara'
]

LAST_NAMES = [
    'Müller', 'Dubois', 'García', 'Rossi', 'Jansen', 'Andersson', 'Novák',
    'Smit', 'Moreau', 'Fernández', 'Ricci', 'Schneider', 'Larsen', 'Nagy',
    'De Jong', 'Hansen', 'Kowalski', 'Martin', 'Weber', 'Vidal'
]

STREETS = [
    'High Street', 'Station Road', 'Rue de la Paix', 'Grand Rue', 
    'Hauptstraße', 'Bahnhofstraße', 'Via Roma', 'Corso Vittorio Emanuele', 
    'Calle Mayor', 'Gran Vía', 'Prinsengracht', 'Keizersgracht'
]

CITIES = [
    'London', 'Berlin', 'Paris', 'Madrid', 'Rome', 
    'Amsterdam', 'Vienna', 'Dublin', 'Brussels', 'Stockholm'
]

COUNTRIES = [
    'United Kingdom', 'Germany', 'France', 'Spain', 'Italy', 
    'Netherlands', 'Austria', 'Ireland', 'Belgium', 'Sweden'
]

POSTCODES = [
    '10115', '75001', '28001', '00185', '1011', '1000', 
    '1010', 'D01', '111 22', 'WC1A', '75002', '10117'
]

SEGMENTS = [
    'Retail', 'Wholesale', 'Corporate', 'Enterprise', 
    'Small Business', 'VIP Member', 'Government/Non-Profit'
]

# Static product references for synthetic data generation
PRODUCTS = [
    ("4K Ultra HD Smart TV (55-inch)", "Electronics", 499.99, 280.00),
    ("Wireless Noise-Canceling Headphones", "Electronics", 199.99, 95.00),
    ("Mechanical Gaming Keyboard", "Electronics", 89.99, 38.00),
    ("Ergonomic Wireless Mouse", "Electronics", 49.99, 18.00),
    ("USB-C Multi-Port Adapter", "Electronics", 29.99, 9.50),
    ("Cotton Crewneck T-Shirt", "Apparel", 24.99, 6.00),
    ("Slim-Fit Denim Jeans", "Apparel", 64.99, 21.00),
    ("Fleece Zip-Up Hoodie", "Apparel", 54.99, 18.00),
    ("Water-Resistant Windbreaker", "Apparel", 89.99, 32.00),
    ("Stainless Steel Pour-Over Kettle", "Home & Kitchen", 44.99, 15.00),
    ("Cast Iron Skillet (10-inch)", "Home & Kitchen", 39.99, 14.00),
    ("Air Fryer Oven", "Home & Kitchen", 119.99, 52.00),
]

# Order constants
NUM_ORDERS = 1000

ORDER_STATUSES = ["Completed", "Completed", "Completed", "Pending", "Cancelled"]

PAYMENT_METHODS = ["Credit Card", "Debit Card", "PayPal", "Apple Pay"]

START_DATE = "2025-01-01"

END_DATE = "2026-08-31"

# Return constants
RETURN_RATE = 0.08

RETURN_REASONS = [
    "Defective / Damaged",
    "Wrong Size / Fit",
    "Item Not as Described",
    "Changed Mind",
    "Late Delivery",
]

RETURN_STATUSES = ["Approved", "Approved", "Approved", "Rejected"]

