import random

class Card:
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    def __str__(self):
        return f"{self.face}{self.suit}"

    def __repr__(self):
        return self.__str__()

class Deck:
    FACES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["♦", "♠", "♥", "♣"]
    JOKERS = [("Joker", "🃏"), ("Joker", "🃏")]
    
    def __init__(self, number_of_decks=1, jokers=False):
        if number_of_decks < 1:
            raise ValueError("Number of decks must be at least 1.")
        
        self.decks = number_of_decks
        self.jokers = jokers
        self._build_deck()
        
            
    def _build_deck(self):
        self.deck = [Card(face, suit) for suit in self.SUITS for face in self.FACES] * self.decks
        
        if self.jokers:
            self.deck.extend(Card(*joker) for joker in self.JOKERS * self.decks)
            
        random.shuffle(self.deck)


    def draw(self, num_cards=1):
        if num_cards > len(self.deck):
            raise ValueError(f"Cannot draw {num_cards} cards. Only {len(self.deck)} remaining.")
        
        return [self.deck.pop() for _ in range(num_cards)]


    def shuffle(self):
        self._build_deck()

    
    def cards_left(self):
        return len(self.deck)

    
    def __len__(self):
        return len(self.deck)


    def __iter__(self):
        return iter(self.deck)
    
    
    def __str__(self):
        return f"Deck with {len(self.deck)} cards: " + ", ".join(str(card) for card in self.deck)


    def __repr__(self):
        return self.__str__()
