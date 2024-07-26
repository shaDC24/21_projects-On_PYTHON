#python -m pip install cryptography
#python3 -m pip install cryptography
# pip3 install cryptography
# pip install cryptography

from cryptography.fernet import Fernet



'''
def write_key():
    key=Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)
        
'''

def load_key():
    file=open("5_password_manager\key.key","rb")
    key=file.read()
    file.close()
    return key


pwd=input("What is the master password?")

key=load_key()+pwd.encode()
fer=Fernet(key)

def view(): 
    with open('5_password_manager\password.txt','r') as f:
        for line in f.readlines():
            data=(line.rstrip())
            user=data.split("|")[0]
            passw=data.split("|")[1]
            print(f"NAME : {user}\nPassWOrd: {(fer.decrypt(passw.encode()).decode())}") 
            
def add():
    name=input("Account name : ")
    pw=input("Pass word: ")
    
    with open('5_password_manager\password.txt','a') as f:
        f.write(name+"|"+str(fer.encrypt(pw.encode()).decode())+"\n")
        
        
while True:
    mode=input("Would you like to add a new password or view existing ones\n v for view \n a for add\n q for quit")
    if mode=="v":
        view()
    elif mode=="a":
        add()
    elif mode=="q":
        quit()
    else:
        print("Invalid mode!!!")
        continue
    