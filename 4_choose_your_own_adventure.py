name=input("Type your name : ")
print(f"Welcome {name} to this adventure!!")

ans=input("You are on a dirt road,\n it has come to an end and you can go left or right. \n Which way you want to go?\n").lower()

if ans=="left":
    ans=input("You have came to a river.\nYou can walk around it or can swim across it.\nWhat will you do?\nType s for swim \n w for walk\n").lower()
    if ans=="s":
        print("You swam across and eaten by an alligator!!!")
    elif ans=="w":
        print("You walk for many miles.Run out of water and you lose the game!!!")
    else:
        print("Not a valid option .You lose!!!")
elif ans=="right":
    ans=input("You have came to a bridge.\nYou can go back or can go across it.\nWhat will you do?\nType c for cross \n b for back\n").lower()
    if ans=="c":
       ans=input("You crossed the bridge and meeet a stranger .Will you talk to him?(y/n)").lower()
       if ans=="y":
           print("You talk to the stanger and you win!!!")
           print("CONGRATULATIONS!!!!")
           quit()
       elif ans=="n":
           print("You ignored the stanger .so you lose !!!")
       else:
            print("Not a valid option .You lose!!!")
           
        
    elif ans=="b":
        print("You go back to the main road. and you lose!!!")
    else:
        print("Not a valid option .You lose!!!")
    
else:
    print("Not a valid option . so You lose!!!")
    
    
print(f"Thank you for trying {name}")    
    