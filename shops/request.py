class Request:

    def __init__(self, txt):
        self._txt = txt.split()
        if len(self._txt) < 4:
            raise ValueError('Некорректный формат ввода')

    @property
    def give(self):
        return {'by': self._txt[4].lower(),
                'to': self._txt[-1].lower(),
                'amount': int(self._txt[1]),
                'product': self._txt[2].lower()}
