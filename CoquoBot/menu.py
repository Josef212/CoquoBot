# TODO: Move this to a db
BASE_MENU = {
    'FigaDeCabra': 2.50,
    'BaconCheddar': 2.50,
    '4Formatges': 2.50,
    'Bbq': 2.50,
    'PolloCurry': 2.50,
    'Carabassó': 2.50,
    'Xampinyons': 2.50,
    'Llonganissa': 2.50,
    'Margarita': 2.50,
    'Pepperoni': 2.50,
    'Nutella': 2.50,
    'Patata': 2.50,
    'FormatgesAmbPera': 2.50,
    'Botifarra': 2.50,
    'Carbonara': 2.50,
    'Alberginia': 2.50,
    'Hawaiana': 2.50,
    #'Salsa-Olivada': 0.0,
    #'Salsa-Pesto': 0.0,
    #'Salsa-Bbq': 0.0,
    #'Salsa-Anxoves': 0.0,
    #'Salsa-MayonesaWasabi': 0.0,
    #'Salsa-Brava': 0.0
}

URL = 'https://coquopizza.com/carta/'

class Menu:
    def __init__(self, app):
        self.menu = BASE_MENU
        self.app = app

    def get_menu_web(self) -> str:
        return URL

    def get_menu_list(self) -> list:
        return list(self.menu.keys())

    def get_item_price(self, item: str) -> float:
        if item in self.menu:
            return self.menu[item]

        self.app.warn(f"Error trying to get a cut of {item} price")
        return 0.0
