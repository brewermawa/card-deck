from collections import Counter
from deck import Deck

class ThreeCardPoker:
    def __init__(self):
        self.deck = Deck()

    
    def deal(self):
        return self.deck.draw(3), self.deck.draw(3)
    

    def is_consecutive(self, values):
        for i in range(1, len(values)):
            if values[i] - values[i-1] == 1:
                if i == len(values) - 1:
                    return True
            else:
                return False


    def _pair_(self, cards):
        faces = [card.face for card in cards]
        if 2 in [v for _, v in Counter(faces).items()]:
            return True
        return False


    def _three_of_a_kind_(self, cards):
        faces = [card.face for card in cards]
        if 3 in [v for _, v in Counter(faces).items()]:
            return True
        return False


    def _straight_(self, cards):
        faces = [card.face for card in cards]

        #1. Convert the values of the cards faces to integers so its possible to sort (J=11, Q=12, K=13, A=1)
        face_values_high_cards = {"J": 11, "Q": 12, "K": 13, "A": 1}
        face_values = [face_values_high_cards[face] if face in face_values_high_cards else int(face) for face in faces]

        #2. Sort the list
        face_values.sort()

        #3. Check if the list is consecutive
        if self.is_consecutive(face_values):
            return True
        
        #4. If there are A's(1) in the list change their value to 14, sort, anch check if it is consecutive
        if 1 in face_values:
            face_values = [14 if face_values[i] == 1 else face_values[i] for i in range(len(face_values))]
            face_values.sort()
            return self.is_consecutive(face_values)
        else:
            return False


    def _flush_(self, cards):
        suits = [card.suit for card in cards]
        if 3 in [v for _, v in Counter(suits).items()]:
            return True
        return False


    def _straight_flush_(self, cards):
        if self._straight_(cards) and self._flush_(cards):
            return True
        return False


    def _mini_royal_(self, cards):
        faces = [card.face for card in cards]
        if sorted(faces) == ["A", "K", "Q"] and self._flush_(cards):
            return True
        return False


    def _high_card_play_(self, cards):
        faces = [card.face for card in cards] 
    
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


    def play(self, cards):
        hand_check = any([
           self._mini_royal_(cards),
           self._straight_flush_(cards),
           self._flush_(cards),
           self._straight_(cards),
           self._three_of_a_kind_(cards),
           self._pair_(cards),
           self._high_card_play_(cards),
        ])

        return hand_check

        
    def dealer_qualifies(self, cards):
        faces = [card.face for card in cards]
        hand_check = any([
           self._mini_royal_(cards),
           self._straight_flush_(cards),
           self._flush_(cards),
           self._straight_(cards),
           self._three_of_a_kind_(cards),
           self._pair_(cards),
           any([True for face in faces if face in ["Q", "K", "A"]])
        ])
    
        return hand_check


    #compare hands
    def compare_hands(self, player_hand, dealer_hand):
        pass


    def win_amount(self, player_hand):
        pass

