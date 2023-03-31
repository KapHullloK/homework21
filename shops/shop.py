from shops.storage import Storage


class Shope(Storage):

    def __init__(self, items, capacity=20):
        self._items = items
        self._capacity = capacity
        if len(self._items) > 5:
            raise ValueError('Магазин полн')

    def add(self, title, quantity):
        tot_quantity = sum(self._items.values()) + quantity

        if tot_quantity > self._capacity:
            quantity = self._capacity - sum(self._items.values())

        if quantity:
            if title in self._items:
                self._items[title] += quantity
                print(f'Добвалено {title} в размере {quantity}\n'
                      f'Всего {title}: {self._items[title]}')
            else:
                self._items[title] = quantity
                print(f'Новый товар {title} в размере {quantity}')
        else:
            print("Нет мест")

    def remove(self, title, quantity):

        if title in self._items:
            tot_quantity = self._items[title] - quantity

            if tot_quantity < 0:
                quantity = 0

            if quantity:
                self._items[title] -= quantity
                print(f'\nНужное количество есть на складе'
                      f'\nУбрана {title} в размере {quantity}\n')
            else:
                self._items.pop(title)
                print(f'Товар {title} удалён')
        else:
            print("Нет такого товара")

    def get_free_space(self):
        return self._capacity - sum(self._items.values())

    def get_items(self):
        itms = ''

        for k, v in self._items.items():
            itms += f'{k}: {v}\n'

        return itms[:-1]

    def get_unique_items_count(self):
        return len(self._items)
