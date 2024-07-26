import random

user_wins=0
computer_wins=0
options=["r","p","s"]

while True:
    user_input=input("Type\n r for rock\n p for paper\n s for scissor\n Q to quit\n").lower()
    if user_input=="q":
        print(f"You win for {user_wins} times")
        print(f"Computer wins for {computer_wins} times.")
        if(int(user_wins)>int(computer_wins)):
            print("You win!!!!!!")
        else:
            print("Computer wins!!!!")
        quit()
        
    elif user_input not in options:
        continue
    else:
        comp_input=random.randint(0,2)
        # 0=r , 1=p , 2=s
        comp_choose=options[int(comp_input)]
        print(f"computer picked {comp_choose}")
        
        if user_input=="r" and comp_choose=="s":
            print("You won!")
            user_wins+=1
        elif user_input=="p" and comp_choose=="r":
            print("You won!")
            user_wins+=1 
        elif user_input=="s" and comp_choose=="p":
            print("You won!")
            user_wins+=1  
        else:
            print("You loose")
            computer_wins+=1         
        
          
        
    
    