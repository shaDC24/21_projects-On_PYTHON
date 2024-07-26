import random
import string

def generate_password(min_length,numbers=True,specal_charachters=True):
    letters=string.ascii_letters
    digits=string.digits
    specal_char=string.punctuation
    charachters=letters
    
    if numbers:
        charachters+=digits
    if specal_charachters:
        charachters+=specal_char  
        
    pwd= "" 
    meet_criteria=False
    has_number=False
    has_specal_char=False    
    
    while not meet_criteria  or len(pwd)<min_length:
        new_char=random.choice(charachters)
        pwd+=new_char
        if  new_char in digits:
            has_number=True
        if new_char in specal_char:
            has_specal_char=True 
        meet_criteria=True
        if numbers:
            meet_criteria=has_number
        if specal_charachters:
            meet_criteria=  meet_criteria and has_specal_char  
            
            
    return pwd        
                   
            
        
    
min_length=int(input("Enter the minmum length : ")) 
has_number=input("Do you want to have numbers?(y/n)  ").lower() == "y"  
has_special_chars=input("Do you want to have special charachters?(y/n)  ").lower() == "y"  
  
print(f"The generated password is : {generate_password(min_length,has_number,has_special_chars)}")
