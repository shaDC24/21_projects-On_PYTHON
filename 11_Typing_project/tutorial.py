# pip install windows-curses
# python -m install windows-curses
import curses
from curses import wrapper
import time
import random

def start_screen(stdscr):
    stdscr.clear()
    # stdscr.addstr(1,0,'Hello world!') # 1 line down , started with 0th charachter 
    # stdscr.addstr(1,5,'Hello world!') 
    stdscr.addstr(0,0,'Welcome to the speed typing test !!!')
    stdscr.addstr('\nPress any key to begin.') # next line = \n
    stdscr.refresh()
    key=stdscr.getkey()
    print(key)
    
#overlaying text: 
def display_text(stdscr,target_text,current_text,wpm=0):
        stdscr.addstr(target_text)
        stdscr.addstr(1,0,f"WPM : {wpm}")
        
        for i,char in enumerate(current_text):
            correct_char=target_text[i]
            color=curses.color_pair(1)
            if char!=correct_char:
                color=curses.color_pair(2)
            stdscr.addstr(0,i,char,color)    
            
def load_text():
    with open("11_Typing_project/text.txt","r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()    
    
def wpm_test(stdscr):
    target_text = load_text()
    current_text=[]
    wpm=0
    start_time=time.time()
    stdscr.nodelay(True)
    # stdscr.clear()
    # stdscr.addstr(target_text)
    # stdscr.refresh()
    
    while True:
        time_elapsed=max(time.time()-start_time,1)
        wpm=round((len(current_text)/(time_elapsed/60))/5,2)
        stdscr.clear()
        display_text(stdscr,target_text,current_text)
        stdscr.refresh() 
        
        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break
        try:        
            key=stdscr.getkey()
        except:
            continue
        
        if ord(key)==27:
            break
        
        if key in ("KEY_BACKSPACE",'\b','\x7f'):
            if len(current_text)>0:
                current_text.pop()
        elif len(current_text)<len(target_text):        
            current_text.append(key)
        
   
            
           

def main(stdscr):
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_WHITE)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_WHITE)
    # curses.init_pair(3,curses.COLOR_WHITE,curses.COLOR_BLACK)
    start_screen(stdscr)
    
    while True:
        wpm_test(stdscr)
        stdscr(2,0,"You completed the task.Press any key to continue.")
        key = stdscr.getkey()
        
        if ord(key)==27:
            break


wrapper(main)    