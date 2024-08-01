import random
COLORS=["R","G","B","Y","W","O"]
TRIES=10
CODE_LENGTH=4


def generate_code():
    code=[]
    
    for _ in range(CODE_LENGTH):
        color=random.choice(COLORS)
        code.append(color)
        
    return code

def guess_code():
    while True:
        guess=input("Guess : ").upper().split(" ")    
        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors.")
            continue
        
        for color in guess:
            if color not in COLORS:
                print(f"Invelid color {color}.Try again.")
                break
        else:
            break
        return guess
    
def check_code(guess,real_code):
        color_cnt={}
        correct_pos=0
        incorrect_pos=0
        
        for color in real_code:
            if color not in color_cnt:
                color_cnt[color]=0
            color_cnt[color] +=1 
        
        for gss,real_clr in zip(guess,real_code):
               if gss == real_clr:
                   correct_pos+=1
                   color_cnt[gss]-=1
                   
        for gss,real_clr in zip(guess,real_code): 
            if gss in color_cnt and color_cnt[gss]>0:
                incorrect_pos+=1
                color_cnt[gss]-=1
        return correct_pos,incorrect_pos
    
def game():
    print(f"Welcome to the MASTERMIND. You have {TRIES} try to guess...")
    print("The valid colors are : ",*COLORS)
    code=generate_code()
    for attemps in range(1,TRIES+1):
        guess_c=guess_code()
        correct_pos,incorrect_pos=check_code(guess_c,code)
        
        if correct_pos==CODE_LENGTH:
            print(f"You guesses the code in {attemps} tries!!!!")
            break
        
        print(f"Correct Position : {correct_pos} | Incorrect position : {incorrect_pos}")  
    else:
        print(f"You ran out of the tries....The code was : ",*code)              
     
     
if __name__=="__main__":
    game()       
        
         