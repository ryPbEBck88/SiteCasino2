from time import perf_counter
from random import shuffle

start = perf_counter()

meanings_52_sheet = ('A', '2', '3', '4',
                     '5', '6', '7', '8',
                     '9', '10', 'J', 'Q',
                     'K')
suits_52_sheet = {
    'Hearts': '♥',    # Черви
    'Crosses': '♣',   # Крести
    'Diamonds': '♦',   # Бубны
    'Spades': '♠'      # Пики
}


class Card:
    def __init__(self, name, meaning, suit):
        self.name = name
        self.meaning = meaning
        self.suit = suit


class Deck:
    def __init__(self, meanings, suits):
        self.deck = [Card(meaning + suits[suit], meaning, suit) \
                     for suit in suits \
                     for meaning in meanings]

    def shuffle_deck(self):
        shuffle(self.deck)

    def show_cards_top_deck(self, number):
        print(' '.join(card.name for card in self.deck[-number:]))

    def pop_cards_top_deck(self):
        if not self.deck:
            raise IndexError("Cannot pop from an empty deck.")
        return self.deck.pop()

    def distribute_the_boxes(self, number_boxes=1, number_card=5):
        if number_boxes * number_card > len(self.deck):
            raise ValueError("Not enough cards in the deck to distribute.")

        answer = [[] for _ in range(number_boxes)]
        for _ in range(number_card):
            for index in range(number_boxes):
                answer[index].append(self.pop_cards_top_deck().name)
        return answer


deck = Deck(meanings_52_sheet, suits_52_sheet)
deck.shuffle_deck()
# deck.show_cards_top_deck(5)

print(deck.distribute_the_boxes(number_boxes=1))
print(perf_counter() - start)
