print("Welcome to my computer quiz!")
playing=input("Do you want to play?")

if ((playing.lower()!="yes") and (playing.lower()!="y")):
    quit()
 
print("Let's play!")
score=0
ans=input("What does CPU stand for?")
if ans.lower()=="central processing unit" :
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
       
       
ans=input("What does GPU stand for?")
if ans.lower()=="graphics processing unit" :
    print("Correct!")
    score+=1
else:
    print("Incorrect!")



ans=input("What does RAM stand for?")
if ans.lower()=="random access memory" :
    print("Correct!")
    score+=1
else:
    print("Incorrect!")


ans=input("What does PSU stand for?")
if ans.lower()=="power supply unit" :
    print("Correct!")
    score+=1
else:
    print("Incorrect!")  
    
    
                 
print(f"You got {score} questions correct :)")
print(f"You got {(score/4)*100}% :)")

       