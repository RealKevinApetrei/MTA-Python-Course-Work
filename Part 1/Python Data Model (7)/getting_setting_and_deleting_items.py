class Inventory:
    def __init__(self):
        self._products = ["leds", "batteries", "solder"]
        self._prices = [1.00, 3.00, 5.00]

    def __repr__(self):
        product_price_pairs = ("{}:${:.2f}".format(*pair)
                               for pair in zip(self._products, self._prices))
        listing = "\n".join(product_price_pairs)
        return "<Inventory>\n{listing}\n</Inventory>".format(listing=listing)


    def __setitem__(self, key, value):
        if key in self:
            self._prices[self._products.index(key)] = value
        else:
            self._products.append(key)
            self._prices.append(value)

    def __delitem__(self, key):
        try:
            if key in self:
                index = self._products.index(key)
                del self._products[index]
                del self._prices[index]
            else:
                raise KeyError()
        except KeyError:
            print("That product does not exist!")
            

    def __getitem__(self, key):
        for index, product in enumerate(self._products):
            if product == key:
                return self._prices[index]
        return self.__missing__(key)

    def __contains__(self, key):
        return key in self._products

    def __missing__(self, notfoundkey):
        return "We are currently out of stock. Please let us know how we can help!"



inventory = Inventory()
