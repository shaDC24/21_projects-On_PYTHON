import random

# random.randrange(start=-1,stop=10)
# r=random.randrange(-5,11)
# print(f"Range : {r}")

# r=random.randint(-5,11)
# print(f"Int : {r}")

top_of_range=(input("Type a number : "))

if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    if top_of_range<=0:
        print("Please input a number larger than 0 next time!")
        quit()
else:
    print("You should input a valid number !")
    quit()
        
    
r=random.randint(0,top_of_range)
guesses=0



while True:
    guesses+=1
    user_guess=input("Guess a number : ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
        if user_guess<=0:
                print("Please input a number larger than 0 next time!")
                continue
    else:
        print("You should input a valid number !")
        continue
    
    if(user_guess==r):
        print("You got it right")
        print(f"You have guessed for {guesses} times.")
        quit()
    elif user_guess<r:
        print("You got it wrong :(")
        print("Try again") 
        print("Input larger value")    
    else:
        print("You got it wrong :(")
        print("Try again") 
        print("INput smaller value!")   
    
    
