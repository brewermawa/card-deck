import three_card_poker

"""
    1. Deal three cards to the player
    2. Deal three cards to the dealer
    3. Check if fold or play
    4. Check in dealer qualifies
    5. Compare player and dealer hands
"""

player, dealer = three_card_poker.deal()

#print(f"Dealer: {dealer}")
print(f"Player: {player}")

print("Play") if three_card_poker.play(player) else print ("Fold")

