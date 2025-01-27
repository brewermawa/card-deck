import sys
from three_card_poker import ThreeCardPoker

play = 0
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
print(f"Played: {play}")