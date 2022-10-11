## Itemis coding challenge - Sales Taxes


### Documentation:

The sales taxes task is written in Python. I used Python version 3.9.
The project doesn't use external pip packages.

The package contains a helper.py file for helping functions. The taxes.py is the main file for the taxes package. It contains a Taxes class which accepts a taxed items list, so that users can add more items to an already calculated sales-taxes-list.

The import_json_data method imports the items that need to be calculated to the self.items class variable. It accepts either a pathlib.PurePath to the JSON file or a python list containing the items.
Format for JSON or list:

    [
        {
            'item_id': str,
            'imported': bool,
            'count': int
        },
    ]

Same applies to the import_products_data method. It imports products from a python list or JSON file to the self.products class variable. It also accepts either a pathlib.PurePath to the JSON file or a python list containing items.
Format for JSON or list:

    [
        {
            'id': str,
            'name': str,
            'price': str,
            'tag': str
        },
    ]

The calculate_single_items method calculates the sales taxes with given arguments for one item and returns the item object as python dict.

Required arguments are:

-   tag: str
-   price: str
-   imported: bool.

Optional arguments are:

-   name: str
-   count: int

If name is not specified, name will be "item" by default. If count is not specified, the default count will be 1.

The calculate_items method accepts an items list with same format as specified above. The items argument is optional and if not specified uses self.items instead.
The calculate_items method loops through the items, calculates the taxes for every item in the list and returns the taxed_items as a python dict.

The print_str method creates a string with the format from the coding challenge file output from this challenge for all calculated items in the class instance and returns it.

---

### Why json and not command line input, text file or string?

You said, that I should write the code, so that it could fit a production environment. The code isn't perfect and I changed some things every day because I didn't know if you wanted me to use a command line input or input the data with the input string you specified in the challenge, but in the end I thought I just give you a production environment answer of how I would do it. So why JSON? Because this would be the only thing that would fit. Get data from the database and parse it to a json file or python dict and then just loop through the items and products. No company would parse a string or .txt file to some API or App when there is a database from which data could be parsed to a JSON or JSON like format (python dict).
