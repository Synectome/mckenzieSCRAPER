class Item:

    def __init__(self, name, description, id, price, price_updated):
        self.id = id
        self.name = ""
        self.description = ""
        self.price = price
        self.price_updated = price_updated

    def get_price(self, new_price, current_time):
        self.price = new_price
        self.price_updated = current_time