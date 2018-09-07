#!/usr/bin/env python
"""A deck as a collection of cards.

author: alvaro salgado
salgado.alvaro@me.com
"""
import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck(object):
    """Class for creating a french deck."""

    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        """Initialize deck.

        self._cards is a list (because of the square brackets after the =)
        """
        self._cards = [Card(rank, suit)
                       for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        """Use 'len' function."""
        return len(self._cards)

    def __getitem__(self, position):
        """Use 'getitem' to enable indexing."""
        return self._cards[position]

beer_card = Card('7', 'diamonds')
beer_card

deck = FrenchDeck()
print(len(deck))
# type(deck)
deck[0]
deck[-1]

choice(deck)

deck[:3]

deck[12::13]

for card in deck:
    print(card)

Card('Q', 'hearts') in deck

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    """Sorts deck."""
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

card = Card('Q', 'clubs')
card.rank
FrenchDeck.ranks.index(card.rank)

spades_high(card)

for card in sorted(deck, key=spades_high):
    print(card)
