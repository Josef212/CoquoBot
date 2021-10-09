from order import Order

class OrderManager:
    def __init__(self):
        self.orders = {}
    
    def get_order(self, id: str) -> Order:
        if id not in self.orders:
            self.orders[id] = Order()
        
        return self.orders[id]

    def reset_order(self, id: str) -> None:
        self.get_order(id).reset()