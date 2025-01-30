from collections import Counter
from deck import Deck


class Hand:
    def __init__(self, cards):
        self.cards = cards
        self.rank = 0


class ThreeCardPoker:
    def __init__(self):
        self.deck = Deck()

    
    def deal(self):
        return self.deck.draw(3)
    

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


    def play(self, hand):
        hand_check = any([
           self._straight_flush_(hand),
           self._three_of_a_kind_(hand),
           self._straight_(hand),
           self._flush_(hand),
           self._pair_(hand),
           self._high_card_play_(hand),
        ])

        return hand_check

        
    def dealer_qualifies(self, hand):
        faces = [card.face for card in hand.cards]
        hand_check = any([
           self._straight_flush_(hand),
           self._flush_(hand),
           self._straight_(hand),
           self._three_of_a_kind_(hand),
           self._pair_(hand),
           any([True for face in faces if face in ["Q", "K", "A"]])
        ])
    
        return hand_check


    """
    compare_hands 
    Recieves both player and dealear hands and compares the initial hand ranks.
    Returns 0 if the dealer wins
    Returns 1 if the player wins
    Returns 2 in the comparison is a tie
    """
    def compare_hands(self, player_hand, dealer_hand):
        if player_hand.rank < dealer_hand.rank:
            #Dealer wins
            return 0
        elif player_hand.rank > dealer_hand.rank:
            #Player wins
            return 1
        else:
            #Initial rank tie

            player_faces = [card.face for card in player_hand.cards]
            dealer_faces = [card.face for card in dealer_hand.cards]

            #print("----------")
            #print(f"Dealer faces: {dealer_faces}")
            #print(f"Player faces: {player_faces}")

            face_values_high_cards = {"J": 11, "Q": 12, "K": 13, "A": 14}
            dealer_face_values = sorted([face_values_high_cards[face] if face in face_values_high_cards else int(face) for face in dealer_faces])
            player_face_values = sorted([face_values_high_cards[face] if face in face_values_high_cards else int(face) for face in player_faces])

            #Tie on high card
            if player_hand.rank == 0:
                dealer_face_values.reverse()
                player_face_values.reverse()

                for i in range(len(player_face_values)):
                    if dealer_face_values[i] > player_face_values[i]:
                        return 0
                    if dealer_face_values[i] < player_face_values[i]:
                        return 1    
                return 2

            if player_hand.rank == 1:
                #Both dealer and player have a pair
                #print(f"Dealer face values: {dealer_face_values}")
                #print(f"Player face values: {player_face_values}")

                dealer_pair = [k for k, v in Counter(dealer_face_values).items() if v == 2][0]
                player_pair = [k for k, v in Counter(player_face_values).items() if v == 2][0]

                if dealer_pair > player_pair:
                    return 0
                
                if dealer_pair < player_pair:
                    return 1
                
                dealer_other_card = [k for k, v in Counter(dealer_face_values).items() if v == 1][0]
                player_other_card = [k for k, v in Counter(player_face_values).items() if v == 1][0]

                if dealer_other_card > player_other_card:
                    return 0
                
                if dealer_other_card < player_other_card:
                    return 1
                
                return 2

            if player_hand.rank == 2:
                dealer_face_values.reverse()
                player_face_values.reverse()

                for i in range(len(player_face_values)):
                    if dealer_face_values[i] > player_face_values[i]:
                        return 0
                    if dealer_face_values[i] < player_face_values[i]:
                        return 1    
                return 2
            
            if player_hand.rank == 3 or player_hand.rank == 5:
                #dealer_face_values.reverse()
                #player_face_values.reverse()

                #If there is an A on a hand, check if there is a 2, if there is, change the 14 to a 1
                if 14 in dealer_face_values and 2 in dealer_face_values:
                    dealer_face_values[dealer_face_values.index(14)] = 1
                    dealer_face_values.sort()

                if 14 in player_face_values and 2 in player_face_values:
                    player_face_values[player_face_values.index(14)] = 1
                    player_face_values.sort()
                
                if dealer_face_values[0] > player_face_values[0]:
                    return 0
                elif dealer_face_values[0] < player_face_values[0]:
                    return 1
                
                return 2

            if player_hand.rank == 4:
                #Both dealer and player have a three of a kind
            
                if dealer_face_values[0] > player_face_values[0]:
                    return 0
                
                return 1
            

    """
    Regardless of the dealer's hand, if the player has a straight, three of a kind or a
    straight flush, the player gets an ante bonus
    """
    def ante_bonus(self, hand):
        rank_values = {3: 1, 4: 4, 5: 5}
        return rank_values.get(hand.rank, 0)
