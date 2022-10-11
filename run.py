from taxes.helpers import *
from taxes.taxes import Taxes
from pathlib import Path

root_folder = Path(__file__).parents[0]

def run():
    tax_string = 'Output 1:\n'
    taxes1 = Taxes()
    taxes1.import_json_data(root_folder / 'data/input 1.json')
    taxes1.import_products_data(root_folder / 'data/products.json')
    taxes1.calculate_items()
    tax_string += f'{taxes1.print_str()}\n\n'

    tax_string += 'Output 2:\n'
    taxes2 = Taxes()
    taxes2.import_json_data(root_folder / 'data/input 2.json')
    taxes2.import_products_data(root_folder / 'data/products.json')
    taxes2.calculate_items()
    tax_string += f'{taxes2.print_str()}\n\n'

    tax_string += 'Output 3:\n'
    taxes3 = Taxes()
    taxes3.import_json_data(root_folder / 'data/input 3.json')
    taxes3.import_products_data(root_folder / 'data/products.json')
    taxes3.calculate_items()
    tax_string += f'{taxes3.print_str()}\n\n'

    print(tax_string)


if __name__ == '__main__':
    run()
