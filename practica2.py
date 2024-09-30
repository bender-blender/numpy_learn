

import numpy as np
from random import choices
# TODO Карточная растасовка


def suit(name):
    """
    Масть
    """
    pictures = {f"6 {name}": 6, f"7 {name}": 7, f"8 {name}": 8, f"9 {name}": 9,
                f"10 {name}": 10, f"Валет {name}": 11, f"Дама {name}": 12,
                f"Король {name}": 13, f"Туз {name}": 14}
    return pictures


heart = suit("Черва")
peak = suit("Пика")
tambourine = suit("Бубна")
cross = suit("Крест")

class Deck:
    """
    Колода
    """
    __deck = np.array([[i for i in heart.keys()], [i for i in peak.keys()], [
                i for i in tambourine.keys()], [i for i in cross.keys()]])
    def shuffle(self):
        """
        Растасовка
        """
        res = []
        for i in self.__deck:
            for x in i:
                res.append(x)
        deck = np.array(res)
        np.random.shuffle(deck)
        return deck
    

d = Deck().shuffle()
print(d)