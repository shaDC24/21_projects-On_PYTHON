import random

MAX_LINES=3
MAX_BET=100
MIN_BET=1

ROWS=3
COLS=3

symbol_count={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}
symbol_value={
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns=[]    
    for col in range(cols):
        column=[]
        current_symbols=all_symbols[:]
        for row in range(rows):
             value=random.choice(current_symbols)  
             current_symbols.remove(value)
             column.append(value) 
             
        columns.append(column)  
    return columns       
     
def check_winning(columns,lines,bet,values):
    winnings=0
    winnings_lines=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if(symbol!=symbol_to_check):
                break
        else:
            winnings+=(values[symbol]*bet)
            winnings_lines.append(line+1)
    return winnings,winnings_lines    

    
         
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,col in enumerate(columns):
            if i != len(col)-1:
                print(col[row],end="|")
            else:
                print(col[row],end="")
        print("\n")        
            

def deposit():
    while True:
        amount=input("What would you like to deposit? $")
        if(amount.isdigit()):
            amount=int(amount)
            if amount>0:
                break
            else:
                print("Amount must be greater then 0")
        else:
            print("Please enter a number.")
    return amount 


def get_no_of_lines():
    while True:
        amount=input(f"Enter the number of lines to bet on (1-{MAX_LINES})?")
        if(amount.isdigit()):
            amount=int(amount)
            if 1<=amount<=MAX_LINES:
                break
            else:
                print("Enter a valid number.")
        else:
            print("Please enter a number.")
    return amount  

def get_bet():
    while True:
        amount=input(f"What would you like to bet?$")
        if(amount.isdigit()):
            amount=int(amount)
            if MIN_BET<=amount<=MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} and {MAX_BET}")
        else:
            print("Please enter a number.")
    return amount 

def spin(balance):
    
    lines=get_no_of_lines()
    while True:
        bet=get_bet()
        total_bets=bet*lines
        print(f"You are betting {bet} on {lines} lines.Total bet is {total_bets}")
        if total_bets>balance:
            print(f"You dont have enough balance to bet that amount.Your current balance is {balance}.But you want to bet {total_bets}")
        else:
            break
    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)  
    winnngs,winning_lines = check_winning(slots,lines,bet,symbol_value)
    print(f"YOu won {winnngs}") 
    print(f"You won on ",winning_lines) 
    return winnngs-total_bets
    
           
def main():
    balance=deposit()
    while True:
        print(f"Current balance is ${balance}")
        ans=input("Press enter to spin or q to quit.")
        if ans=='q':
            break
        balance+=spin(balance)
    print(f"You left with {balance}")    
    
   
    
main()   
        
            