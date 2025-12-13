class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, qty):
        if qty < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = qty
