# Blackjack
This is a tiny blackjack game I made 

Iterations

First round = win if get over 18 but less than 
21, ace is just one 

Second round = win if get over 18 but less than 21, print out 
king, queen, jack, ace is just one

3rd round = win if get over 18 but les than 21, 
ace can be 1 or 11 --> have to decide before 

4th round = add dealer deck 
dealer will only hit as many times as user
and will stop hitting if greater than 16
will win if greater than dealer 
and doesn't bust

5th round --> Did not think black jack would be this complicated
break this into functions

main 
deck 
dpoints
dhit 
phit 
points 

player turn function
inputs points, phit 
outputs points, phit as a tuple

dealer turn function
inputs dpoints, dhit
outputs dpoints, dhit as a tuple 

card drawing function 
input deck 
outputs card and deck 

score deciding function 
input points, dpoints, phit
output points, dpoints, phit

6th edit -> While loop to deal with errors instead of ending game directly

7th edit -> Allow to use ace whenever they want
not sure how will do this

8th edit -> improve ui 
line breaks
better waits 
better wording in display messages!
Additional waits 

9th edit -> 
Multiplayer?????? 
That will be another day lol 
Will need to have a player class and a dealer class for this 