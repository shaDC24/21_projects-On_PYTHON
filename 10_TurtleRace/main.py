import turtle
import time
import random

WIDTH,HEIGHT=700,500
COLORS=['red','green','blue','cyan','black','brown','pink','yellow','coral','orange']


def get_number_of_racers():
    racers=0
    while True:
        racers=input("Enter the number of racers (2-10) : ")
        
        if racers.isdigit():
            racers=int(racers)
            if 2<=racers<=10:
                return racers
            else:
                print("Enter valid number from 2 to 10.")
        else:
            print("Input is not numeric...Try again!")
            
 
def init_turtle():
    screen=turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title('Turtle racing!')

   
def create_turtles(colors):
    turtles=[] 
    spacingx=WIDTH//(len(colors)+1)
    for i,colr in enumerate(colors):
        racer=turtle.Turtle()
        racer.color(colr)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        #set pos
        racer.setpos(-WIDTH//2 + (i+1)*spacingx,-HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles    
    
            
def race():
    racers=get_number_of_racers()  
    init_turtle()
    random.shuffle(COLORS)
    colors=COLORS[:racers]
    turtles=create_turtles(colors)
    while True:
        for racer in turtles:
           distance=random.randrange(1,20)
           racer.forward(distance)
           x,y=racer.pos()
           if y>=(HEIGHT//2-10):
               return colors[turtles.index(racer)]
           
              
print(f"{race()} turtle has win the game!!")


# racer=turtle.Turtle()
# racer.speed(1)
# racer.penup()
# racer.pendown()
# racer.shape('turtle')
# racer.color('red')
# racer.forward(100)   
# racer.left(90)
# racer.forward(100)
# racer.right(90)
# racer.backward(100)    
# time.sleep(5)
                    
            