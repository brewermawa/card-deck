from five_card_poker import play

hands = int(input("Enter number of hands: "))

for key, value in play(hands).items():
    match key:
        case 0: print(f"Nothing: {value}")
        case 1: print(f"Pairs: {value}")
        case 2: print(f"Two pairs: {value}")
        case 3: print(f"3 of a kind: {value}")
        case 4: print(f"Straight: {value}")
        case 5: print(f"Flush: {value}")
        case 6: print(f"Full house: {value}")
        case 7: print(f"Poker: {value}")
        case 8: print(f"Straight flush: {value}")
        case 9: print(f"Royal flush: {value}")