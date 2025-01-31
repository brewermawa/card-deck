from deck import Deck
from three_card_poker_new import ThreeCardPoker, Hand

bank = 100
ante = 5

playing_deck = Deck()

player_hand = Hand(playing_deck.draw(3))
dealer_hand = Hand(playing_deck.draw(3))

tcp = ThreeCardPoker(player_hand, dealer_hand)

print(tcp.play())

if tcp.play() != "xxx":
    bank += ante * tcp.play()
    
print(f"Bank: {bank}")
