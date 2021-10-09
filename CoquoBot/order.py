from menu import Menu

class Order:
    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self.order = {}

    def add_to_order(self, user: str, item: str, amount: int) -> None:
        if user not in self.order:
            self.order[user] = {}

        user_order = self.order[user]
        if item not in user_order:
            user_order[item] = 0

        user_order[item] += amount

        if user_order[item] < 0:
            user_order[item] = 0

    def get_user_order(self, user: str) -> dict:
        if user not in self.order:
            return {}
        
        return self.order[user]

    def get_full_order(self, menu: Menu) -> dict:
        ret = {}
        cart = {}

        for user in self.order:
            user_order = self.order[user]

            for item in user_order:
                if not item in cart:
                    cart[item] = 0
                
                cart[item] += user_order[item]
        
        total_price = self.__get_cart_price(cart, menu)
        
        ret["cart"] = cart
        ret["total"] = total_price

        return ret

    def get_user_order(self, menu: Menu, user: str) -> dict:
        ret = {}
        cart = {}
        total_price = 0.0

        if user in self.order:
            user_order = self.order[user]

            for item in user_order:
                if not item in cart:
                    cart[item] = 0
                
                cart[item] += user_order[item]
            
            total_price = self.__get_cart_price(cart, menu)

        ret["cart"] = cart
        ret["total"] = total_price

        return ret

    def __get_cart_price(self, cart: dict, menu: Menu) -> float:
        total_price = 0.0

        for item in cart:
            item_amount = cart[item]
            item_price = menu.get_item_price(item)
            item_total_price = item_amount * item_price
            total_price += item_total_price
        
        return total_price
