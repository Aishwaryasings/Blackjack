from os import remove
import random
import time


def dealer_turn(deck, dpoints, dealer_hit):
    """
    Runs dealer's turn
    Parameter deck: deck of cards (array)
    Parameter dpoints: dealer's points (int)
    Parameter dealer_hit: will dealer hit or stay (bool)
    Returns deck, dpoints, dealer_hit
    """

    print("Now it's the dealer's turn") 
    if dealer_hit == 1: 
        deck, card1 = remove_card(deck, "The Dealer", dpoints)
        dpoints = dpoints + int(card1)
        if dpoints > 16: 
            dealer_hit = 0

    else: 
        print("The Dealer Has Chosen To Stay")
    print("As a reminder, the dealer's total points is "+str(dpoints))
    return deck, dpoints, dealer_hit

def player_turn(deck, points, player_hit):
    """
    Runs player's turn
    Parameter deck: deck of cards (array)
    Parameter points: dealer's points (int)
    Returns deck, dpoints, player_hit (will game error out or not --> bool)
    """
    print("It's your turn!")
    error = 0
    if player_hit == 1: 
        deck, car = remove_card(deck, "You")
        if car == -1:
            player_hit = 1
            error = 1
            return deck, points, error
        else: 
            points = points + int(car)
            time.sleep(3)
    else: 
        print("You had chosen to stay!")
    print("Your Total Points Is "+str(points))
    return deck, points, error, player_hit 



def remove_card(deck, player, points = 0):
    """
    Removes card from deck
    Parameter deck: deck of cards (array)
    Parameter player: you or the dealer(string)
    Paramater points: optional only for dealer
    Returns deck, card (int from deck)
    Preconditions: player can be you or the dealer, points = 0 if player is you
    """
    
    assert player == "You" or player == "The Dealer", "player parameter should be either You or The Dealer"
    if player == "You": 
        assert points == 0
    
    print("We are going to remove a card for "+player + "!")
    time.sleep(3)
    card = deck.pop(random.randint(0,len(deck)-1))
    
    #ace for player 
    if card == 1 and player == "you": 
        inp = int(input(player+ " got an Ace! Do you want it to be a 1 or 11? "))
        if inp == 1: 
            card = 1
        elif inp == 11:
            card = 11
        else: 
            print("Error! Did not type in 1 or 11! End of Game!")
            card = -1
    
    #ace for dealer 
    elif card == 1 and player == "the dealer":
        if points > 12: 
            card = 1
        else: 
            card = 11
    
    elif card >= 2 and card <= 9:
        print(player + " got a "+ str(card))
    #card for jack, king, queen 
    elif card == 10: 
        print(player + " got a Jack!")
    elif card == 11: 
        print(player + " got a Queen!")
        card = 10
    else: 
        print(player + " got a King!")
        card = 10
    return deck, card


def bust_check(points, dpoints):
    """
    Checks if bust
    Parameter points: player's points (int)
    Paramater dpoints: dealer's points (int)
    Returns bool (whether bust or not)
    """
    if points > 21 and dpoints > 21: 
        print("Both you and the dealer have busted")
        return False
    elif points > 21: 
        print("You have busted! You have lost! Sorry!")
        return False
    elif dpoints > 21: 
        print("The dealer has busted! You have won! Great job!")
        return False
    return True

def ask_hit():
    inp = input("Do you want to hit or stay? Type Hit or Stay exactly ")
    time.sleep(1)
    print("You said: "+str(inp))
    time.sleep(3)
    return inp

def determine_winner(points, dpoints):
    if points > dpoints: 
        print("You've won! Great job!")
    elif points < dpoints: 
        print("You lost to the dealer! Sorry")
    else:
        print("You tied!")

def next_round(points, dpoints, player_hit, dealer_hit):
    """
    Checks if there will be next round
    Parameter points: player's points (int)
    Paramater dpoints: dealer's points (int)
    Returns player_hit (bool) --> if next round or not
    """
    error = 0
    assert player_hit == 0 or player_hit == 1, "player"
    assert dealer_hit == 0 or dealer_hit == 1, "dealer"
    if player_hit == 1 and dealer_hit == 0: 
        inp = ask_hit()
        if inp == "Stay":
            player_hit = 0
            determine_winner(points, dpoints)
        elif inp == "Hit":
            pass
        else:
            print("Error! Wrong Input! End of Game!")
            error = 1
    elif player_hit == 1 and dealer_hit == 1:
        inp = ask_hit()
        if inp == "Stay":
            player_hit = 0
        elif inp == "Hit":
            pass
        else:
            print("Error! Wrong Input! End of Game!")
            error = 1
    elif player_hit == 0 and dealer_hit == 0: 
        determine_winner(points, dpoints)
    elif player_hit == 0 and dealer_hit == 1: 
        pass
    else: 
        print("Error! Wrong CHEESE! End of Game!")
        error = 1
    return player_hit, dealer_hit, error

if __name__ == "__main__":
    """
    main function 
    runs the whole game
    """
                                   #jacks     #queen   #king
    deck = (list(range(1,10)) * 4) + [10]*3 + [11]*4 + [12]*4
    points = 0
    dpoints = 0
    dealer_hit = 1
    player_hit = 1

    while player_hit == 1 or dealer_hit == 1:

        print("Let's start this round!")

        #player turn
        deck, points, error, player_hit = player_turn(deck, points, player_hit)
        if error == 1: 
            break
        #dealer turn
        deck, dpoints, dealer_hit = dealer_turn(deck, dpoints, dealer_hit)

        #bust check
        if bust_check(points, dpoints) == False: 
            break
        
        #next round? 
        player_hit, dealer_hit, error = next_round(points, dpoints, player_hit, dealer_hit)
        if error == 1: 
            break

        
    time.sleep(3)
    print("Good Game!")



        



