from three_card_poker import ThreeCardPoker

tcp = ThreeCardPoker()

dealer, player = tcp.draw()

#print(f"Dealer cards: {dealer}")
print(f"Player cards: {player}")


while True:
    tcp = ThreeCardPoker()

    dealer, player = tcp.draw()

    print(f"Player cards: {player}")
    if tcp.play(player):
        break
