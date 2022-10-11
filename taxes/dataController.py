import json
from pathlib import Path

root_folder = Path(__file__).parents[1]

# Get products from products.json
products = open(root_folder / 'data/products.json')
PRODUCTS = json.load(products)
products.close()

# Get carts data from data.json
data = open(root_folder / 'data/input 1.json')
DATA = json.load(data)
data.close()