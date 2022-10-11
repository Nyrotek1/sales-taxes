import json
from taxes.helpers import *
from math import ceil
from decimal import Decimal


class Taxes():
    """Class for calculating taxes for given items and printing / outputting them.
    'items' can be given to add items to an existing dictionary and needs to have
    following keys specified: 'items': [], 'taxes': '0.00', 'total': '0.00'"""

    def __init__(self, taxed_items=None):
        if taxed_items:
            value_error_catch(taxed_items, 'items', dict)

        self.taxed_items = taxed_items if taxed_items else {
            'items': [],
            'taxes': '0.00',
            'total': '0.00'
        }
        self.last_item = {}
        self.products = None
        self.items = None
        self.cart = None

    def import_json_data(self, file_path) -> list:
        """Imports the data from a JSON file into a list for the current class instance and also returns the list.
        JSON needs to be array of item objects containing at least:  
        'item_id': str, 'imported': bool and 'count': int"""
        items = open(file_path)
        self.items = json.load(items)
        items.close()
        return self.items

    def import_products_data(self, file_path) -> list:
        """Imports the products from a JSON file into a list for the current class instance and also returns the list.
        JSON needs to be array of item objects containing at least: 
        'id': str, 'name': str, 'price': str and 'tag': str"""
        products = open(file_path)
        self.products = json.load(products)
        products.close()
        return self.products

    def import_txt_data(self, file_path):
        pass

    def import_str_data(self, data_str):
        pass

    def export_taxes_json(self, file_path):
        pass

    def calculate_single_item(self, tag: str, price: str, imported: bool, name='item', count=1) -> dict:
        """Calculates taxes with given arguments. Returns dict with name, count, taxes and taxed price. 
        If name is not specified, default name will be 'item'. If count is not specified, default count will be 1.
        An exception will be thrown if the arguments got the wrong type. 'tag', 'price', 'name' need to be string.
        'imported' needs to be boolean."""
        value_error_catch(tag, 'tag', str)
        value_error_catch(price, 'price', str)
        value_error_catch(imported, 'imported', bool)
        value_error_catch(name, 'name', str)
        value_error_catch(count, 'count', int)

        taxed = None

        if (
            tag != 'book'
            and tag != 'medical product'
            and tag != 'food'
        ):
            taxed = True

        if not taxed and imported:
            result = Decimal(price) * Decimal(5) / Decimal(100)
        elif taxed and not imported:  # Taxed and not imported
            result = Decimal(price) * Decimal(10) / Decimal(100)
        elif taxed and imported:  # Taxed and imported
            result = Decimal(price) * Decimal(15) / Decimal(100)
        else:  # Not taxed and not imported
            result = Decimal(0)

        result = Decimal(ceil(result * Decimal(20)) / Decimal(20))

        taxes = result * Decimal(count)
        taxed_price = (result + Decimal(price)) * Decimal(count)

        self.last_item = {
            'name': name,
            'count': count,
            'imported': imported,
            'taxes': f"{taxes:.2f}",
            'taxed_price': f"{taxed_price:.2f}"
        }

        self.taxed_items['items'].append(self.last_item)
        self.taxed_items['taxes'] = f"{Decimal(self.taxed_items['taxes']) + taxes:.2f}"

        self.taxed_items['total'] = f"{Decimal(self.taxed_items['total']) + taxed_price:.2f}"

        return self.last_item

    def calculate_items(self, items = None):
        if not isinstance(items, list) and not isinstance(self.items, list):
            raise Exception(f'items argument is {items} and imported JSON items is {self.items}. one of both must be a valid list type!')
        elif not isinstance(items, list) and isinstance(self.items, list):
            items = self.items
        else:
            pass

        if not isinstance(self.products, list):
            raise Exception(f'imported JSON products is {self.products}. please import JSON products before calculating items.')

        for item in items:
            product = find_product_by_id(item['item_id'], self.products)
            self.calculate_single_item(
                product['tag'],
                product['price'],
                item['imported'],
                product['name'],
                item['count']
            )
        
        return self.taxed_items

    def print_str(self) -> str:
        """Creates a simple formatted string for all items, that can be printed or written in a text file."""

        taxed = self.taxed_items

        tax_res = ''
        for item in taxed['items']:
            tax_res += f"{item['count']} "
            if item['imported']:
                tax_res += 'imported '
            tax_res += f"{item['name']}: {item['taxed_price']}\n"

        tax_res += f"Sales Taxes: {taxed['taxes']}\nTotal: {taxed['total']}"
        return tax_res
