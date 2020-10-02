from Item import Item


class Auction:

    def __init__(self, title, id, url):
        self.title = title
        self.date = 0
        self.items = dict()
        self.id = id
        self.url = url

    def add_item(self, name, description):
        self.items[id] = Item(name, description, id)

    def remove_item(self, id):
        del self.items[id]

    def set_date(self, date):
        self.date = date

    def get_title(self):
        return self.title

    def get_date(self):
        return self.title

    def get_id(self):
        return self.id

    def get_url(self):
        return self.url

    def get_item_names(self):
        return self.items.keys()

    def get_items(self):
        return self.items

    def __repr__(self):
        print(str(self.title))
        print("ID : " + str(self.id))
        print("URL : " + str(self.url))
        print("End Date : " + str(self.date))
        print("Items list : " + str(self.items.keys()))
        return 'end of auction'
