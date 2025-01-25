from collections import Counter
from deck import Deck
import sys


def is_consecutive(values):
    for i in range(1, len(values)):
        if values[i] - values[i-1] == 1:
            if i == len(values) - 1:
                return True
        else:
            return False


def straight(faces):
    #faces = ["10", "K", "A", "Q", "J"]

    #1. Convert the values of the cards faces to integers so its possible to sort (J=11, Q=12, K=13, A=1)
    face_values_high_cards = {"J": 11, "Q": 12, "K": 13, "A": 1}
    face_values = [face_values_high_cards[face] if face in face_values_high_cards else int(face) for face in faces]

    #2. Sort the list
    face_values.sort()

    #3. Check if the list is consecutive
    if is_consecutive(face_values):
        return True

    #4. If there are A's(1) in the list change their value to 14, sort, anch check if it is consecutive
    if 1 in face_values:
        face_values = [14 if face_values[i] == 1 else face_values[i] for i in range(len(face_values))]
        face_values.sort()
        return is_consecutive(face_values)
    else:
        return False
        

def result(cards):
    faces = [card.face for card in cards]
    suits = [card.suit for card in cards]

    #faces = ["J", "Q", "K", "A", "10"]
    #suits = ["♦", "♦", "F", "♦", "♦"]

    face_count = [v for _, v in Counter(faces).items()]
    
    """
        0: Nothing
        1: Pair
        2: Two Pair
        3: Three of a kind
        4: Straight
        5: Flush
        6: Full House
        7: Four of a Kind
        8: Straight Flush
        9: Royal Flush
    """
    
    #Pair or Full House
    if face_count.count(2) == 1:
        return 6 if face_count.count(3) == 1 else 1
    
    #Two pairs
    if face_count.count(2) == 2:
        return 2

    #Three of a kind
    if face_count.count(3):
        return 3
    
    #Poker
    if face_count.count(4):
        return 7
    
    suits_count = [v for _, v in Counter(suits).items()]

    #Royal Flush
    #print(faces)
    if sorted(faces) == ['10', 'A', 'J', 'K', 'Q'] and suits_count.count(5):
        return 9

    #Straight Flush
    if straight(faces) and suits_count.count(5):
        return 8
    
    #Straight
    if straight(faces):
        return 4
    
    #Flush
    if suits_count.count(5):
        return 5 

    return 0


def play(number_of_hands):
    results = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

    for i in range(number_of_hands):
        sys.stdout.write(f"Hand: {i}\r")
        sys.stdout.flush()
        
        playing_deck = Deck(1)
        r = result(playing_deck.draw(5))
        results[r] += 1

    return results

""" i = 0

while True:
    i += 1
    sys.stdout.write(f"Hand: {i}\r")
    sys.stdout.flush()
    
    playing_deck = Deck(1)
    player_cards = playing_deck.draw(5)
    r = result(player_cards)

    if r == 9:
        print(f"I took {i} hands to get a royal flush")
        print(player_cards)
        break

    if i == 1000000:
        print("A million hands and still no royal flush")
        break """

#print(f"Result: {r}")
