class Hat:
    # Hats_id_counter = 0

    def __init__(self, id, topping, supplier, quantity):
        # maybe we need casting here.
        self.id = id
        self.topping = topping
        self.supplier = supplier
        self.quantity = quantity


class Supplier:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Order:
    def __init__(self, location, hat):
        self.location = location
        self.hat = hat
