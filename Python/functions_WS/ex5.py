# Approved by: Arin

def discount(dict):
    """ Return given dictionary of products with 10% sale price """
    return {product: price*0.9 for product, price in dict.items()}


if __name__ == "__main__":
    dict = {
        "car": 80000,
        "TaylorSwiftTicket": 30367,
        "iphone": 1964,
        "devops": 10,
        "book": 7555.52
    }
    print("Discounted dict:", discount(dict))