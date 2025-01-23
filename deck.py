import random

class Card:
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    def __str__(self):
        return f"{self.face}{self.suit}"

class Deck:
    def __init__(self, number_of_decks=1):
        faces = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
        suits = ["♦", "♠", "♥", "♣"]

        self.deck = [Card(face, suit) for suit in suits for face in faces]
        self.shuffle()

    def draw(self):
        return self.deck.pop()

    def shuffle(self):
        random.shuffle(self.deck)
    
    def cards_left(self):
        return len(self.deck)