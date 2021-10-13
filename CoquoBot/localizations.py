# TODO: Move this to a db, drive or whatever

from loc_keys import LocKeys

CAT = {
    # Cmd start
    LocKeys.START_MSG: 'Arrancant el bot...',

    # Cmd coquo
    LocKeys.COQUO_OPTIONS: 'Com et pot ajudar el CoquoBot?',
    LocKeys.COQUO_FINISHED: 'Gràcies per utilitzar CoquoBot :D',

    # Cmd get order
    LocKeys.GET_ORDER_TITLE_FULL_ORDER: 'Total de la comanda:',
    LocKeys.GET_ORDER_TITLE_GET_USERS: 'Comanda de @{0}:',
    LocKeys.GET_ORDER_MISSING_PRICE: '[NOTA]: Un o varis elements no tenen preu!',
    LocKeys.GET_ORDER_TOTAL_PRICE: 'Preu total',
    LocKeys.GET_ORDER_MISSING_ARGS: 'Nombre d\'arguments invàlid. Falta el nom de l\'usuari',
    LocKeys.GET_ORDER_TOO_MUCH_ARGS: 'Nombre d\'arguments invàlid. Massa arguments, només és necessari el nom d\'usuari',

    # Cmd order
    LocKeys.ORDER_FINISH_TITLE: 'Comanda per @{0} registrada:',
    LocKeys.ORDER_MSG: 'Selecciona talls per afegir-los a la teva comanda',
    LocKeys.ORDER_ITEM_ADDED: '{0} afegit a la comanda',

    # Cmd reset order 
    LocKeys.ORDER_RESET_DONE: 'La comanda per aquest grup s\'ha reiniciat.',

    # Cmd edit order
    LocKeys.EDIT_ORDER_TITLE_UPDATED: 'La comanda per @{0} s\'ha actualitzat',
    LocKeys.EDIT_ORDER_USER_ORDER: 'Modificant la comanda de @{0}',
    LocKeys.EDIT_ORDER_EMPTY: 'No s\'han afegit elements a la teva comanda. Utilitza [order] per iniciar una comanda',

    # Cmd add order
    LocKeys.ADD_ORDER_MISSING_ARGS: 'Nombre d\'arguments invàlid. És necessari un nom d\'usuari i un tall com a mínim.',
    LocKeys.ADD_ORDER_ITEMS_ADDED: 'S\'ha demanat per @{0}',

    # Cmd add order me
    LocKeys.ADD_ORDER_ME_MISSING_ARGS: 'Nombre d\'arguments invàlid. És necessari un tall com a mínim.',

    # Cmd info
    LocKeys.INFO_SCHEDULE: 'Horari: Dimecres a Diumenge 19:00 to 24:00',

    # Btn
    LocKeys.BTN_MENU: 'Menú',
    LocKeys.BTN_WEB: 'Menú Web',
    LocKeys.BTN_ORDER: 'Fer comanda',
    LocKeys.BTN_EDIT_ORDER: 'Modificar comanda',
    LocKeys.BTN_GET_FULL_ORDER: 'Llista completa',
    LocKeys.BTN_GET_MY_ORDER: 'La meva comanda',
    LocKeys.BTN_FINISH: 'Tancar :)',

    LocKeys.BTN_RESET_ORDER: '-Reset full order-',
}

ES = {
    # Cmd start
    LocKeys.START_MSG: 'Arrancando el bot...',

    # Cmd coquo
    LocKeys.COQUO_OPTIONS: '¿Como CoquoBot te puede ayudar?',
    LocKeys.COQUO_FINISHED: 'Gracias por usar CoquoBot :D',

    # Cmd get order
    LocKeys.GET_ORDER_TITLE_FULL_ORDER: 'Total del pedido:',
    LocKeys.GET_ORDER_TITLE_GET_USERS: 'Pedido de @{0}:',
    LocKeys.GET_ORDER_MISSING_PRICE: '[NOTA]: Uno o varios elementos no tienen precio!',
    LocKeys.GET_ORDER_TOTAL_PRICE: 'Precio total',
    LocKeys.GET_ORDER_MISSING_ARGS: 'Número de argumentos invalido. Falta el nombre de usuario',
    LocKeys.GET_ORDER_TOO_MUCH_ARGS: 'Número de argumentos invalido. Demasiados argumentos, sólo es necesario el nombre del usuario',

    # Cmd order
    LocKeys.ORDER_FINISH_TITLE: 'Comanda para @{0} registrada:',
    LocKeys.ORDER_MSG: 'Selecciona trozos para añadirlos a tu pedido',
    LocKeys.ORDER_ITEM_ADDED: '{0} añadido a la comanda',

    # Cmd reset order 
    LocKeys.ORDER_RESET_DONE: 'El pedido para este grupo se ha reiniciado',

    # Cmd edit order
    LocKeys.EDIT_ORDER_TITLE_UPDATED: 'El pedido de @{0} se ha actualizado',
    LocKeys.EDIT_ORDER_USER_ORDER: 'Modificando pedido de @{0}',
    LocKeys.EDIT_ORDER_EMPTY: 'No se han añadido elementos al pedido. Usa [order] para iniciar un pedido',

    # Cmd add order
    LocKeys.ADD_ORDER_MISSING_ARGS: 'Número de argumentos invalido. Se necesita un nombre de usuario y un trozo como mínimo',
    LocKeys.ADD_ORDER_ITEMS_ADDED: 'Se ha pedido para @{0}',

    # Cmd add order me
    LocKeys.ADD_ORDER_ME_MISSING_ARGS: 'Número de argumentos invalido. Se necesita un trozo como mínimo',

    # Cmd info
    LocKeys.INFO_SCHEDULE: 'Horario: Miercoles a Domingo 19:00 to 24:00',

    # Btn
    LocKeys.BTN_MENU: 'Menú',
    LocKeys.BTN_WEB: 'Menú Web',
    LocKeys.BTN_ORDER: 'Hacer pedido',
    LocKeys.BTN_EDIT_ORDER: 'Modificar pedido',
    LocKeys.BTN_GET_FULL_ORDER: 'Lista completa',
    LocKeys.BTN_GET_MY_ORDER: 'Mi pedido',
    LocKeys.BTN_FINISH: 'Cerrar :)',

    LocKeys.BTN_RESET_ORDER: '-Reset full order-',
}

EN = {
    # Cmd start
    LocKeys.START_MSG: 'Starting the bot...',

    # Cmd coquo
    LocKeys.COQUO_OPTIONS: 'How can CoquoBot help you?',
    LocKeys.COQUO_FINISHED: 'Thank you for using CoquoBot :D',

    # Cmd get order
    LocKeys.GET_ORDER_TITLE_FULL_ORDER: 'Total order:',
    LocKeys.GET_ORDER_TITLE_GET_USERS: '@{0}\'s order:',
    LocKeys.GET_ORDER_MISSING_PRICE: '[NOTE]: One or more items on the cart are missing price!',
    LocKeys.GET_ORDER_TOTAL_PRICE: 'Total price',
    LocKeys.GET_ORDER_MISSING_ARGS: 'Invalid arg count. Missing user\'s name',
    LocKeys.GET_ORDER_TOO_MUCH_ARGS: 'Invalid arg count. Too many argumanets, only username is needed',

    # Cmd order
    LocKeys.ORDER_FINISH_TITLE: 'Order for @{0} registered:',
    LocKeys.ORDER_MSG: 'Click to add items to your cart',
    LocKeys.ORDER_ITEM_ADDED: '{0} added to cart',

    # Cmd reset order 
    LocKeys.ORDER_RESET_DONE: 'Order for this chat has been reset, cart now is empty.',

    # Cmd edit order
    LocKeys.EDIT_ORDER_TITLE_UPDATED: 'Order for @{0} has been updated:',
    LocKeys.EDIT_ORDER_USER_ORDER: 'Editing @{0}\'s order:',
    LocKeys.EDIT_ORDER_EMPTY: 'No items added yet. Use order command to place a fresh order',

    # Cmd add order
    LocKeys.ADD_ORDER_MISSING_ARGS: 'Invalid arg count. A username and at least one item is required',
    LocKeys.ADD_ORDER_ITEMS_ADDED: 'Items added for @{0}',

    # Cmd add order me
    LocKeys.ADD_ORDER_ME_MISSING_ARGS: 'Invalid arg count. At least one item is required',

    # Cmd info
    LocKeys.INFO_SCHEDULE: 'Schedule: Wednesday to Sunday 19:00 to 24:00',

    # Btn
    LocKeys.BTN_MENU: 'Menu',
    LocKeys.BTN_WEB: 'Web menu',
    LocKeys.BTN_ORDER: 'Place order',
    LocKeys.BTN_EDIT_ORDER: 'Edit order',
    LocKeys.BTN_GET_FULL_ORDER: 'Full order',
    LocKeys.BTN_GET_MY_ORDER: 'My order',
    LocKeys.BTN_FINISH: 'Finish :)',

    LocKeys.BTN_RESET_ORDER: '-Reset full order-',
}
