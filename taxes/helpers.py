def value_error_catch(input: object, name: str, var_type: type):
    """ Throws an TypeError with following message if given object is not of given type:
    '{name}={input} needs to be {var_type} but got {type(input)} instead'
    """
    if isinstance(input, var_type):
        return True
    else:
        raise TypeError(
            f'{name}={input} needs to be {var_type} but got {type(input)} instead')


def find_product_by_id(id, products):
    """ Return the product matching the given id
    """
    for product in products:
        if product['id'] == id:
            return product
