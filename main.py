from shops.shop import Shope
from shops.store import Store
from shops.request import Request


def main():
    shop = Shope(items={
        "печеньки": 1,
        "собачки": 5,
        "коробки": 10
    })
    store = Store(items={
        "печеньки": 5,
        "собачки": 5,
        "яблоки": 20
    })

    print(f'Склад:\n{store.get_items()}\n\nМагазин:\n{shop.get_items()}\n')
    print('Формат ввода должен быть такой:\nДоставить 7 собачки из склад в магазин\n')

    request = Request(input()).give

    if request['to'] == 'магазин':
        store.remove(request['product'], request['amount'])
        shop.add(request['product'], request['amount'])
        print(f'\nВ {request["by"]} хранится:\n\n{store.get_items()}')
        return f'\nВ {request["to"]} хранится:\n\n{shop.get_items()}'

    if request['to'] == 'склад':
        shop.remove(request['product'], request['amount'])
        store.add(request['product'], request['amount'])
        print(f'\nВ {request["by"]} хранится:\n\n{shop.get_items()}')
        return f'\nВ {request["to"]} хранится:\n\n{store.get_items()}'


print(main())
