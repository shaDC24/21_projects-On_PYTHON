import curses
from curses import wrapper
import queue
import time
#using bfs we will find the shortest path
maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

# here #=obstacle O=start  X=end

def find_start(maze,start):
    for i,row in enumerate(maze):
        for j,value in enumerate(row):
            if value==start:
                return i,j
    return None
def find_path(maze,stdscr):
    start="O"
    end="X"
    start_pos=find_start(maze,start)
    q=queue.Queue()
    q.put((start_pos,[start_pos]))
    visited=set()
    
    while not q.empty():
        current_pos,path=q.get()
        row,col=current_pos
        
        stdscr.clear()
        print_maze(maze,stdscr,path)
        time.sleep(0.3)
        stdscr.refresh()
        
        if maze[row][col] == end:
            return path
        
        
        neighbours=find_neighbours(maze,row,col)
        
        for nbr in neighbours:
            if nbr in visited:
                continue
            r,c=nbr
            if maze[r][c] == "#":
                continue
            newpath=path+[nbr]
            q.put((nbr,newpath))
            visited.add(nbr)
        
        
def find_neighbours(maze,row,col):
    neighbours=[]
    
    if row>0:
        neighbours.append((row-1,col))
        
    if row+1<len(maze):
        neighbours.append((row+1,col))  
    
    if col>0:
        neighbours.append((row,col-1))
        
    if col+1<len(maze[0]):
        neighbours.append((row,col+1)) 
        
        
    return neighbours              
                
    
    

def print_maze(maze,stdscr,path=[]):
    BLUE=curses.color_pair(1)
    RED=curses.color_pair(2)
    
    for i,row in enumerate(maze):
        for j,value in enumerate(row):
            if (i,j) in path:
                stdscr.addstr(i,j*2,"X",RED)
            else:
                stdscr.addstr(i,j*2,value,BLUE )
           
def main(stdscr):
    #making a color
    curses.init_pair(1,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_YELLOW,curses.COLOR_BLACK)
    #magenta_and_cyan=curses.color_pair(1)
    
    # stdscr.clear()
    # #stdscr.addstr(5,5,"Hello world!")
    # #stdscr.addstr(5,0,"Hello world!")
    # #stdscr.addstr(5,0,"Hello world!",magenta_and_cyan)
    # print_maze(maze,stdscr)
    # stdscr.refresh()
    find_path(maze,stdscr)
    stdscr.getch()
    
    
wrapper(main)    
    