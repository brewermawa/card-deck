from collections import Counter
from deck import Deck

def straight(faces):
    #faces = ["5", "3", "A", "4", "6"]
    
    face_values = []
    for face in faces:
        if face == "J":
            face_values.append(11)
        elif face == "Q":
            face_values.append(12)
        elif face == "K":
            face_values.append(13)
        elif face == "A":
            face_values.append(1)
        else:
            face_values.append(int(face))

    #print(faces)
    face_values.sort()
    #print(face_values)

    for i in range(1, len(face_values)):
        if face_values[i] != face_values[i - 1] + 1:
            #print("No straight")
            break
        else:
            return True
            #print("STRAIGHT")
            #break
    
    if 1 in face_values:
        for i in range(0, len(face_values)-1):
            if face_values[i] == 1:
                face_values[i] = 14

    face_values.sort()
    #print(face_values)

    for i in range(1, len(face_values)):
        if face_values[i] != face_values[i - 1] + 1:
            return False
            #print("No straight")
            #break
        else:
            continue

    return True
        

def result(cards):
    faces = [card.face for card in cards]
    suits = [card.suit for card in cards]

    faces = ["5", "8", "A", "4", "2"]
    suits = ["♦", "♦", "♦", "♦", "♦"]

    #print(faces)
    #print(Counter(faces).items())

    face_count = [v for _, v in Counter(faces).items()]
    
    #print(face_count)
    """
        0: Nothing
        1: Pair
        2: Two Pair
        3: Three of a kind
        4: Straight
        5: Flush
        6: Full House
        7: Four of a King
        8: Straight Flush
        9: Royal Flush
    """

    
    #check for pair, if there is 1 pair check is there is a 3 of a kind, if there is, we have a full house
    if face_count.count(2) == 1:
        return 6 if face_count.count(3) == 1 else 1
    
    #check for 2 pairs
    if face_count.count(2) == 2:
        return 2

    #check for 3 of a kind (i already checked for a full house in ase of a pair, no need to check again)
    if face_count.count(3) == 1:
        return 3
    
    #check for poker
    if face_count.count(4) == 1:
        return 7
    

    s = straight(faces)

    suits_count = [v for _, v in Counter(suits).items()]

    if s:
        if suits_count.count(5) == 1:
            return 8
        
        return 4

    if suits_count.count(5) == 1:
        return 5
        
    
    
    return 0
    
    
    #print(suits)

playing_deck = Deck(1)
player_cards = playing_deck.draw(5)

print(player_cards)
print(f"Result: {result(player_cards)}")
