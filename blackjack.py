import random
import time

def remove_card(deck, player):
    print("We are going to remove a card for "+player + "!")
    time.sleep(3)
    card = deck.pop(random.randint(0,len(deck)-1))
    if card == 1: 
        inp = int(input(player+ " got an Ace! Do you want it to be a 1 or 11? "))
        if inp == 1: 
            card = 1
        elif inp == 11:
            card = 11
        else: 
            print("Error! Did not type in 1 or 11! End of Game!")
            card = -1
    elif card >= 2 and card <= 9:
        print(player + " got a "+ str(card))
    elif card == 10: 
        print(player + " got a Jack!")
    elif card == 11: 
        print(player + " got a Queen!")
        card = 10
    else: 
        print(player + " got a King!")
        card = 10
    return deck, card

if __name__ == "__main__":
                                   #jacks     #queen   #king
    deck = (list(range(1,10)) * 4) + [10]*3 + [11]*4 + [12]*4
    points = 0
    dpoints = 0
    dealer_hit = 1
    player_hit = 1

    while player_hit == 1:

    
    
    #player card
    
    points = points + int(card)
    time.sleep(3)
    print("Your Total Points Is "+str(points))

    #dealer's turn
    print("Now it's the dealer's turn") 
    if dealer_hit == 1: 
        
        print("We are going to remove a card for you!")
        time.sleep(3)
        dcard = deck.pop(random.randint(0,len(deck)-1))
        if dcard == 1: 
            inp = input("Do you want it to be a 1 or 11? ")
            if inp == 1: 
                dcard = 1
            elif inp == 11:
                dcard = 11
            else: 
                print("Error! Did not type in 1 or 11! End of Game!")
                player_hit = 0
        elif dcard >= 2 and dcard <= 9:
            print("You got a "+ str(dcard))
        elif dcard == 10: 
            print("You got a Jack!")
        elif dcard == 11: 
            print("You got a Queen!")
            dcard = 10
        else: 
            print("You got a King!")
            dcard = 10
        dpoints = dpoints + int(dcard)
        time.sleep(3)
        print("The Dealer's Total Points Is "+str(dpoints))
        if dpoints > 16: 
            dealer_hit = 0
    else: 
        print("The Dealer Has Chosen To Stay")
        print("As a reminder, the dealer's total points is "+str(dpoints))

    #bust check
    time.sleep(3)
    if points > 21 and dpoints > 21: 
        print("Both you and the dealer have busted")
        break
    elif points > 21: 
        print("You have busted! You have lost! Sorry!")
        break
    elif dpoints > 21: 
        print("The dealer has busted! You have won! Great job!")
        break

    #next round? 
    else: 
        inp = input("Do you want to hit or stay? Type Hit or Stay exactly ")
        time.sleep(1)
        print("You said: "+str(inp))
        time.sleep(3)
        #if stay, decide who wins
        if inp == "Stay":
            player_hit = 0
            if points > dpoints: 
                print("You've won! Great job!")
            elif points < dpoints: 
                print("You lost to the dealer! Sorry")
            else:
                print("You tied!")
        elif inp == "Hit":
            player_hit = 1
        else:
            print("Error! Wrong Input! End of Game!")
            player_hit = 0
time.sleep(3)
print("Good Game!")



        



