from collections import Counter
from deck import Deck


def print_player_cards(cards):
    for card in cards:
        print(card)


def check_pair(cards):
    faces = [card.face for card in cards]

    doubles = []
    for face, count in Counter(faces).items():
        doubles.extend([face] if count == 2 else [])

    return len(doubles)

def check_trips(cards):
    faces = [card.face for card in cards]

    trips = []
    for face, count in Counter(faces).items():
        trips.extend([face] if count == 3 else [])

    return len(trips)


def check_poker(cards):
    faces = [card.face for card in cards]
    #faces = [2, 2, 2, 2, 9]

    poker = []
    for face, count in Counter(faces).items():
        poker.extend([face] if count == 4 else [])

    return len(poker)




pairs = 0
two_pairs = 0
trips = 0
poker = 0

for _ in range(10000):
    playing_deck = Deck(1)
    player_cards = playing_deck.draw(5)

    if check_pair(player_cards) == 1:
        pairs += 1
    elif check_pair(player_cards) == 2:
        two_pairs += 1

    trips += check_trips(player_cards)
    poker += check_poker(player_cards)

print(f"Pairs: {pairs}")
print(f"Two pairs: {two_pairs}")
print(f"Trips: {trips}")
print(f"Poker: {poker}")
