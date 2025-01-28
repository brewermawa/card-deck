import sys
from three_card_poker import ThreeCardPoker

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

tcp = ThreeCardPoker()

#1. Ask for initial bank (assume integer, will add error handling later)
#bank = int(input("Enter initial bank: "))
bank = 1000

#2. Ask for ante amount 
#ante = int(input("Enter ante: "))
ante = 5

#3. Deal cards to player and dealer

dealer, player = tcp.deal()

#4. Check if player plays or folds
if not(tcp.play(player)):
    #5. If player folds deduct ante amount from bank, end hand
    bank -= ante
else:
    #7. Check if dealer qualifies
    if not(tcp.dealer_qualifies(dealer)):
        #8. If dealer does not qualify add ante amount to bank, end hand
        bank += ante
    else:
        #9. If dealer qualifies

        #10. Set addional bet equal to ante amount
        bet = ante

        player_wins = tcp.compare_hands(player, dealer)

        if not(player_wins):
            #11. If dealer wins, deduct ante and bet amount from bank, end hand
            bank -= (ante + bet)
        else:
            #12. If player wins, get pay amount, add it to bank, end hand
            bank += ante
            bank += tcp.win_amount(player)

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