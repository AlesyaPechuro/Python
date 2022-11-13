# ДЗ итератор колоды карт 52 штуки. при вызове некст дает следующую карту и в конце ошибку стопитерейшн


class CardDeck:
    def __init__(self):
        self.cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'валет', 'дама', 'король', 'туз']
        self.suit = ['трефа', 'бубна', 'пика', 'черва']
        self.length = 52
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.length:
            self.index += 1
            for i in self.cards:
                for g in self.suit:
                    print(i, g)
                    if self.index < self.length:
                        self.index += 1
                    else:
                        raise StopIteration


cards_ = CardDeck()
print(next(cards_))
