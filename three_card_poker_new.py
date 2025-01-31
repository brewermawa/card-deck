from collections import Counter
from deck import Deck


class Hand:
    def __init__(self, cards):
        self.cards = cards
        self.rank = 0

    def __str__(self):
        return f"{self.cards}"
    

class ThreeCardPoker:
    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer

        print(f"Player: {self.player}")
        print(f"Dealer: {self.dealer}")


    def play(self):
        
        if not(self._player_plays_()):
            #Player has less than Q-6-4, player looses 1 bet amount, return -1
            return -1
        else:
            if not(self._dealer_qualifies_()):
                #Dealer does not qualify, player wins 1 bet amount, return 1
                return 1
            else:
                #Dealer qualifies, compare hands, return 2 bet amounts if player wins, otherwise -2 bet amounts

                return -100
        
        return "xxx"
    

    def _player_plays_(self):
        hand_check = any([
           self._straight_flush_(self.player),
           self._three_of_a_kind_(self.player),
           self._straight_(self.player),
           self._flush_(self.player),
           self._pair_(self.player),
           self._high_card_play_(self.player),
        ])

        return hand_check
    

    def _dealer_qualifies_(self):
        faces = [card.face for card in self.dealer.cards]
        hand_check = any([
           self._straight_flush_(self.dealer),
           self._flush_(self.dealer),
           self._straight_(self.dealer),
           self._three_of_a_kind_(self.dealer),
           self._pair_(self.dealer),
           any([True for face in faces if face in ["Q", "K", "A"]])
        ])

        return hand_check
    

    def is_consecutive(self, values):
        for i in range(1, len(values)):
            if values[i] - values[i-1] == 1:
                if i == len(values) - 1:
                    return True
            else:
                return False


    def _high_card_play_(self, hand):
        faces = [card.face for card in hand.cards] 
    
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


    def _pair_(self, hand):
        faces = [card.face for card in hand.cards]
        if 2 in [v for _, v in Counter(faces).items()]:
            hand.rank = 1
            return True
        return False

    
    def _flush_(self, hand):
        if hand.rank == 5:
            return False
        
        suits = [card.suit for card in hand.cards]
        if 3 in [v for _, v in Counter(suits).items()]:
            hand.rank = 2
            return True
        return False
    

    def _straight_(self, hand):
        if hand.rank == 5:
            return False
        
        faces = [card.face for card in hand.cards]

        #1. Convert the values of the cards faces to integers so its possible to sort (J=11, Q=12, K=13, A=1)
        face_values_high_cards = {"J": 11, "Q": 12, "K": 13, "A": 1}
        face_values = [face_values_high_cards[face] if face in face_values_high_cards else int(face) for face in faces]

        #2. Sort the list
        face_values.sort()

        #3. Check if the list is consecutive
        if self.is_consecutive(face_values):
            hand.rank = 3
            return True
        
        #4. If there are A's(1) in the list change their value to 14, sort, anch check if it is consecutive
        if 1 in face_values:
            face_values = [14 if face_values[i] == 1 else face_values[i] for i in range(len(face_values))]
            face_values.sort()
            if self.is_consecutive(face_values):
                hand.rank = 3
                return True
            else:
                return False
        else:
            return False
    
    
    def _three_of_a_kind_(self, hand):
        faces = [card.face for card in hand.cards]
        if 3 in [v for _, v in Counter(faces).items()]:
            hand.rank = 4
            return True
        return False


    def _straight_flush_(self, hand):
        if self._straight_(hand) and self._flush_(hand):
            hand.rank = 5
            return True
        return False

