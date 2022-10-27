import random
import time

#All the things I need to make a blackjack game
#1) a deck of cards - array of 1 to 10 with enough 10s to correspond to kings and queens and jacks)
#3) player points - int
#4) player hit - boolean 

deck = (list(range(1,10)) * 4) + [10]*12 #need 12 10s cuz jack, king, queen 4 times
points = 0
player_hit = 1

while player_hit == 1:
    print("We are going to remove a card for you!")
    time.sleep(3)
    card = deck.pop(random.randint(0,len(deck)-1))
    print("You got a "+ str(card))
    points = points + int(card)
    time.sleep(3)
    print("Your Total Points Is "+str(points))
    time.sleep(3)
    if points > 21:
        print("You Lost! Sorry!")
        break
    elif points > 18: 
        print("You Won!") 
        break
    else: 
        inp = input("Do you want to hit or stay? Type Hit or Stay exactly ")
        time.sleep(1)
        print("You said: "+str(inp))
        time.sleep(3)
        if inp == "Stay":
            print("You stayed but still lost! Sorry!")
            player_hit = 0
        elif inp == "Hit":
            player_hit = 1
        else:
            print("Error! Wrong Input! End of Game!")
            player_hit = 0
time.sleep(3)
print("Good Game!")

        



