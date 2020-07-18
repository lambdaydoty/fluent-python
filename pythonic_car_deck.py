"""
Pythonic
"""
import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    """
    FrenchDeck
    """
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades dimonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


beer_card = Card('7', 'diamonds')

deck = FrenchDeck()

print(beer_card)
print(len(deck))
print(deck[-1])

print('')

print(choice(deck))
print(choice(deck))

print('')

print(deck[:5])
print(deck[:5:1])
print(deck[:5:5])

print('')

suit_values = dict(spades=3, hearts=2, dimonds=1, clubs=0)

def spades_high(card):
    """
    comparator for card
    """
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)
