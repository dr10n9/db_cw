class GuitarController:
    def __init__(self, collection=None, manufaturer=None, model=None, price=None):
        self.collection = collection
        self.manufacturer = manufaturer
        self.model = model
        self.price = price
        """"""

    def save(self):
        self.collection.insert_one({
            'manufacturer': self.manufacturer,
            'model': self.model,
            'price': self.price
        })