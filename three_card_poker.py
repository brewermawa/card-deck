from deck import Deck


def deal():
    playing_deck = Deck()
    
    return playing_deck.draw(3), playing_deck.draw(3)


def play(cards):
    faces = [card.face for card in cards]
    
    faces = ["3", "6", "Q"]


    if any([True for face in faces if face in ["K", "A"]]):
        return True
    elif "Q" in faces:
        faces.remove("Q")
        if any([True for face in faces if face in ["7", "8", "9", "10", "J", "Q"]]):
            return True
        if "6" in faces:
            faces.remove("6")
            return True if faces[0] in ["4", "5"] else False
        else:
            return False
    else:
        return False
