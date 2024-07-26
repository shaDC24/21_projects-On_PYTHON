import random
import time

operators=['+','-','/','*']
min_operand=3
max_operand=12
total_problems=10

def generate_problem(min_operand,max_operand):
    left=random.randint(min_operand,max_operand)
    right=random.randint(min_operand,max_operand)
    operator=random.choice(operators)
    exp=str(left)+" "+operator+" "+str(right)
    answer=eval(exp)
    return exp,answer




wrong=0
input("Press enter to start!")
print("---------------------")
start_time=time.time()
for i in range(total_problems):
    exp,answer=generate_problem(min_operand,max_operand)
    while True:
        guess=input(f"Problem {i+1}. {exp} = ")
        if guess==str(answer):
            break
        else:
            wrong+=1
end_time=time.time()
total_time=round(end_time+start_time,2)          
print("---------------------")  
print(f"Nice work! You finished in {total_time} seconds!")      