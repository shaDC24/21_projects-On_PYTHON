import random

def roll():
    min_value=1
    max_value=6
    roll=random.randint(min_value,max_value)
    return roll

while True:
    players=input("Enter the number of players (2-4) : ")
    if players.isdigit():
        players=int(players)
        if 2<=players<=4:
            break
        else:
            print("Must between 2 to 4 players")
            
    else:
        print("Invalid , try again")
            
            
max_score=50
player_score=[0 for _ in range(players)]  


while max(player_score) < max_score:
    
    for player_idx in range(players):
        print(f"\nPlayer {player_idx+1} turn has just started!\n")
        current_score=0
        
        while True:
            should_roll=input("Would you like to roll (y)?")
            if should_roll.lower()!="y":
                break
            
            value=roll()
            if value==1:
                print("You rolled 1!Turn done!")
                current_score=0
                break
            else:
                current_score+=value
                print(f"you rolled a {value}")
                
            print(f"Your score is {current_score}") 
        
        player_score[player_idx] += current_score
        print(f"\nYour total score is {player_score[player_idx]}\n")  
        
max_score=max(player_score)
winning_idx=player_score.index(max_score)
print(f"\nPlayer number {winning_idx+1} is the winner with a score of : {max_score}\n")             
                
            
                
