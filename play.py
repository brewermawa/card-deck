from deck import Deck

playing_deck = Deck(1)

print(playing_deck.cards_left())

for card in playing_deck.draw(5):
    print(card)
                              
print(playing_deck.cards_left())
