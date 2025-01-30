import sys
from three_card_poker import ThreeCardPoker, Hand

"""
    1. Ask for initial bank
    2. Ask for ante amount 
    3. Deal cards to player and dealer
    4. Check if player plays or folds
        5. If player folds deduct ante amount from bank, end hand
        6. if player plays:
            7. Check if dealer qualifies
                8. If dealer does not qualify add ante amount to bank, end hand
                9. If dealer qualifies
                    10. Set addional bet equal to ante amount
                    10. Compare hands
                        11. If dealer wins, deduct ante and bet amount from bank, end hand
                        12. If player wins, get pay amount, add it to bank, end hand
"""

#1. Ask for initial bank (assume integer, will add error handling later)
#bank = int(input("Enter initial bank: "))
bank = 100

#2. Ask for ante amount 
#ante = int(input("Enter ante: "))
ante = 5

for _ in range(50):

    tcp = ThreeCardPoker()

    #3. Deal cards to player and dealer
    dealer = Hand(tcp.deal())
    player = Hand(tcp.deal())


    """ dealer.cards[0].face = "7"
    dealer.cards[0].suit = "♥"
    dealer.cards[1].face = "K"
    dealer.cards[1].suit = "♥"
    dealer.cards[2].face = "5"
    dealer.cards[2].suit = "♥"

    player.cards[0].face = "2"
    player.cards[0].suit = "♦"
    player.cards[1].face = "8"
    player.cards[1].suit = "♠"
    player.cards[2].face = "6"
    player.cards[2].suit = "♥" """

    #print(f"Dealer: {dealer.cards}")
    #print(f"Player: {player.cards}")

    #4. Check if player.cards plays or folds
    if not(tcp.play(player)):
        #5. If player folds deduct ante amount from bank, end hand
        bank -= ante
    else:
        #7. Check if dealer qualifies
        if not(tcp.dealer_qualifies(dealer)):
            #8. If dealer does not qualify add ante amount to bank, end hand
            bank += ante + ante * tcp.ante_bonus(player)

        else:
            #9. If dealer qualifies

            #10. Set addional bet equal to ante amount
            bet = ante

            result = tcp.compare_hands(player, dealer)

            if result == 0:
                #11. If dealer wins, deduct ante and bet amount from bank, end hand
                bank -= (ante + bet)

                if tcp.ante_bonus(player):
                    bank += ante + ante * tcp.ante_bonus(player)

            elif result == 1:
                #12. If player wins, get pay amount, add it to bank, end hand
                bank += (ante + bet) + ante * tcp.ante_bonus(player)
            else:
                #It is a tie
                bank += ante * tcp.ante_bonus(player)

    print(f"Dealer hand rank: {dealer.cards} {dealer.rank}")
    print(f"Player hand rank: {player.cards} {player.rank}")    
    print(f"Bank: {bank}")
    
print("")
print(f"Bank final: {bank}")
















""" play = 0
fold = 0
i = 0

for _ in range(1000):
    i += 1
    sys.stdout.write(f"Hand: {i}\r")
    sys.stdout.flush()

    tcp = ThreeCardPoker()
    dealer, player = tcp.deal()

    if tcp.play(player):
        play += 1
    else:
        fold += 1

print(f"Folded: {fold}")
print(f"Played: {play}") """