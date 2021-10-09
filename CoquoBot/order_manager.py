from order import Order

class OrderManager:
    def __init__(self):
        self.orders = {}
    
    def get_order(self, id: int) -> Order:
        if id not in self.orders:
            self.orders[id] = Order()
        
        return self.orders[id]

    def reset_order(self, id: int) -> None:
        self.get_order(id).reset()