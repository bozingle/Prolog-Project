import tkinter as tk
import numpy as np
import random
import prologComp as PC

random.seed(None)

class GUI(tk.Frame):
    def __init__(self,main):
        tk.Frame.__init__(self,main)
        self.main = main
        self.main.title('Tetris Anon Version')
        self.main.geometry('300x475')
        #Holds the tetris functions. This avoids the need to make a select function. You can just use an index to call
        #the corresponding function
        self.blockfuncts = [self.Oblock,self.Iblock,self.Sblock,self.Zblock,self.Lblock,self.Jblock,self.Tblock]
        #Used to store the moves in case the user wants to know what moves the tetris solver did and in what order.
        self.moves = []
        self.curboard = np.zeros((4,4))
        #Put the gameboards on the screen.
        self.createWidgets()
        self.gameStart()  

    #Following functions are used to draw the tetris block onto the canvas in the position that the user chooses.
    def Tblock(self, frame, pos, grid, gameboard = None, orient = 1, gameGridBool = False):
        color = 'magenta'
        try:
            if orient == 1:
                if grid != None:
                    frame.itemconfig(grid[pos[1]+3][pos[0]+0], fill=color)
                    frame.itemconfig(grid[pos[1]+3][pos[0]+1], fill=color)
                    frame.itemconfig(grid[pos[1]+3][pos[0]+2], fill=color)
                    frame.itemconfig(grid[pos[1]+2][pos[0]+1], fill=color)
                if gameGridBool:
                    gameboard[pos[1]+3,pos[0]+0] = 1
                    gameboard[pos[1]+3,pos[0]+1] = 1
                    gameboard[pos[1]+3,pos[0]+2] = 1
                    gameboard[pos[1]+2,pos[0]+1] = 1
            elif orient == 2:
                if grid != None:
                    frame.itemconfig(grid[pos[1]+3][pos[0]+1], fill= color)
                    frame.itemconfig(grid[pos[1]+2][pos[0]+1], fill=color)
                    frame.itemconfig(grid[pos[1]+1][pos[0]+1], fill=color)
                    frame.itemconfig(grid[pos[1]+2][pos[0]+0], fill=color)
                if gameGridBool:
                    gameboard[pos[1]+3,pos[0]+1] = 1
                    gameboard[pos[1]+2,pos[0]+1] = 1
                    gameboard[pos[1]+1,pos[0]+1] = 1
                    gameboard[pos[1]+2,pos[0]+0] = 1
            elif orient == 3:
                if grid != None:
                    frame.itemconfig(grid[pos[1]+2][pos[0]+0], fill= color)
                    frame.itemconfig(grid[pos[1]+2][pos[0]+1], fill=color)
                    frame.itemconfig(grid[pos[1]+2][pos[0]+2], fill=color)
                    frame.itemconfig(grid[pos[1]+3][pos[0]+1], fill=color)
                if gameGridBool:
                    gameboard[pos[1]+2,pos[0]+0] = 1
                    gameboard[pos[1]+2,pos[0]+1] = 1
                    gameboard[pos[1]+2,pos[0]+2] = 1
                    gameboard[pos[1]+3,pos[0]+1] = 1
            elif orient == 4:
                if grid != None:
                    frame.itemconfig(grid[pos[1]+3][pos[0]+0], fill= color)
                    frame.itemconfig(grid[pos[1]+2][pos[0]+0], fill=color)
                    frame.itemconfig(grid[pos[1]+1][pos[0]+0], fill=color)
                    frame.itemconfig(grid[pos[1]+2][pos[0]+1], fill=color)
                if gameGridBool:
                    gameboard[pos[1]+3,pos[0]+0] = 1
                    gameboard[pos[1]+2,pos[0]+0] = 1
                    gameboard[pos[1]+1,pos[0]+0] = 1
                    gameboard[pos[1]+2,pos[0]+1] = 1
        except:
            return

    def Sblock(self, frame, pos, grid, gameboard = None,  orient = 1, gameGridBool = False):
        color = 'orange'
        try:
            if orient == 1:
                if grid != None:
                    frame.itemconfig(grid[pos[1]+3][pos[0]+0], fill= color)
                    frame.itemconfig(grid[pos[1]+2][pos[0]+2], fill=color)
                    frame.itemconfig(grid[pos[1]+2][pos[0]+1], fill=color)
                    frame.itemconfig(grid[pos[1]+3][pos[0]+1], fill=color)
                if gameGridBool:
                    gameboard[pos[1]+3,pos[0]+0] = 1
                    gameboard[pos[1]+2,pos[0]+2] = 1
                    gameboard[pos[1]+2,pos[0]+1] = 1
                    gameboard[pos[1]+3,pos[0]+1] = 1
            elif orient == 2:
                if grid != None:
                    frame.itemconfig(grid[pos[1]+3][pos[0]+1], fill= color)
                    frame.itemconfig(grid[pos[1]+2][pos[0]+1], fill=color)
                    frame.itemconfig(grid[pos[1]+2][pos[0]+0], fill=color)
                    frame.itemconfig(grid[pos[1]+1][pos[0]+0], fill=color)
                if gameGridBool:
                    gameboard[pos[1]+3,pos[0]+1] = 1
                    gameboard[pos[1]+2,pos[0]+1] = 1
                    gameboard[pos[1]+2,pos[0]+0] = 1
                    gameboard[pos[1]+1,pos[0]+0] = 1
        except:
            return

    def Zblock(self, frame, pos, grid, gameboard = None, orient = 1, gameGridBool = False):
        color = 'green'
        try:
            if orient == 1:
                if grid != None:
                    frame.itemconfig(grid[pos[1]+2][pos[0]], fill= color)
                    frame.itemconfig(grid[pos[1]+2][pos[0]+1], fill=color)
                    frame.itemconfig(grid[pos[1]+3][pos[0]+1], fill=color)
                    frame.itemconfig(grid[pos[1]+3][pos[0]+2], fill=color)
                if gameGridBool:
                    gameboard[pos[1]+3,pos[0]+1] = 1
                    gameboard[pos[1]+2,pos[0]+0] = 1
                    gameboard[pos[1]+2,pos[0]+1] = 1
                    gameboard[pos[1]+3,pos[0]+2] = 1
            elif orient == 2:
                if grid != None:
                    frame.itemconfig(grid[pos[1]+3][pos[0]+0], fill= color)
                    frame.itemconfig(grid[pos[1]+2][pos[0]+0], fill=color)
                    frame.itemconfig(grid[pos[1]+2][pos[0]+1], fill=color)
                    frame.itemconfig(grid[pos[1]+1][pos[0]+1], fill=color)
                if gameGridBool:
                    gameboard[pos[1]+3,pos[0]+0] = 1
                    gameboard[pos[1]+2,pos[0]+0] = 1
                    gameboard[pos[1]+2,pos[0]+1] = 1
                    gameboard[pos[1]+1,pos[0]+1] = 1
        except:
            return

    def Iblock(self, frame, pos, grid, gameboard = None, orient = 1, gameGridBool = False):
        color = 'teal'
        try:
            if orient == 1:
                if grid != None:
                    frame.itemconfig(grid[pos[1]+3][pos[0]+0], fill = color)
                    frame.itemconfig(grid[pos[1]+2][pos[0]+0], fill=color)
                    frame.itemconfig(grid[pos[1]+1][pos[0]+0], fill=color)
                    frame.itemconfig(grid[pos[1]+0][pos[0]+0], fill=color)
                if gameGridBool:
                    gameboard[pos[1]+3,pos[0]+0] = 1
                    gameboard[pos[1]+2,pos[0]+0] = 1
                    gameboard[pos[1]+1,pos[0]+0] = 1
                    gameboard[pos[1]+0,pos[0]+0] = 1
            elif orient == 2:
                if grid != None:
                    frame.itemconfig(grid[pos[1]+3][pos[0]+0], fill= color)
                    frame.itemconfig(grid[pos[1]+3][pos[0]+3], fill=color)
                    frame.itemconfig(grid[pos[1]+3][pos[0]+2], fill=color)
                    frame.itemconfig(grid[pos[1]+3][pos[0]+1], fill=color)
                if gameGridBool:
                    gameboard[pos[1]+3,pos[0]+0] = 1
                    gameboard[pos[1]+3,pos[0]+3] = 1
                    gameboard[pos[1]+3,pos[0]+2] = 1
                    gameboard[pos[1]+3,pos[0]+1] = 1
        except:
            return

    def Oblock(self, frame, pos, grid, gameboard = None, orient = 1, gameGridBool = False):
        color = 'yellow'
        try:
            if orient == 1:
                if grid != None:
                    frame.itemconfig(grid[pos[1]+3][pos[0]+0], fill=color)
                    frame.itemconfig(grid[pos[1]+3][pos[0]+1], fill=color)
                    frame.itemconfig(grid[pos[1]+2][pos[0]+1], fill=color)
                    frame.itemconfig(grid[pos[1]+2][pos[0]+0], fill=color)
                if gameGridBool:
                    gameboard[pos[1]+3,pos[0]+0] = 1
                    gameboard[pos[1]+3,pos[0]+1] = 1
                    gameboard[pos[1]+2,pos[0]+1] = 1
                    gameboard[pos[1]+2,pos[0]+0] = 1
        except:
            return

    def Jblock(self, frame, pos, grid, gameboard = None, orient = 1, gameGridBool = False):
        color = 'red'
        try:
            if orient == 1:
                if grid != None:
                    frame.itemconfig(grid[pos[1]+3][pos[0]], fill=color)
                    frame.itemconfig(grid[pos[1]+2][pos[0]], fill=color)
                    frame.itemconfig(grid[pos[1]+1][pos[0]], fill=color)
                    frame.itemconfig(grid[pos[1]+1][pos[0]+1], fill=color)
                if gameGridBool:
                    gameboard[pos[1]+3,pos[0]] = 1
                    gameboard[pos[1]+2,pos[0]] = 1
                    gameboard[pos[1]+1,pos[0]] = 1
                    gameboard[pos[1]+1,pos[0]+1] = 1
            elif orient == 2:
                if grid != None:
                    frame.itemconfig(grid[pos[1]+2][pos[0]+0], fill=color)
                    frame.itemconfig(grid[pos[1]+2][pos[0]+1], fill=color)
                    frame.itemconfig(grid[pos[1]+2][pos[0]+2], fill=color)
                    frame.itemconfig(grid[pos[1]+3][pos[0]+2], fill=color)
                if gameGridBool:
                    gameboard[pos[1]+2,pos[0]+0] = 1
                    gameboard[pos[1]+2,pos[0]+1] = 1
                    gameboard[pos[1]+2,pos[0]+2] = 1
                    gameboard[pos[1]+3,pos[0]+2] = 1
            elif orient == 3:
                if grid != None:
                    frame.itemconfig(grid[pos[1]+1][pos[0]+1], fill=color)
                    frame.itemconfig(grid[pos[1]+2][pos[0]+1], fill=color)
                    frame.itemconfig(grid[pos[1]+3][pos[0]+1], fill=color)
                    frame.itemconfig(grid[pos[1]+3][pos[0]], fill=color)
                if gameGridBool:
                    gameboard[pos[1]+1,pos[0]+1] = 1
                    gameboard[pos[1]+2,pos[0]+1] = 1
                    gameboard[pos[1]+3,pos[0]+1] = 1
                    gameboard[pos[1]+3,pos[0]] = 1
            elif orient == 4:
                if grid != None:
                    frame.itemconfig(grid[pos[1]+2][pos[0]], fill=color)
                    frame.itemconfig(grid[pos[1]+3][pos[0]], fill=color)
                    frame.itemconfig(grid[pos[1]+3][pos[0]+1], fill=color)
                    frame.itemconfig(grid[pos[1]+3][pos[0]+2], fill=color)
                if gameGridBool:
                    gameboard[pos[1]+2,pos[0]] = 1
                    gameboard[pos[1]+3,pos[0]] = 1
                    gameboard[pos[1]+3,pos[0]+1] = 1
                    gameboard[pos[1]+3,pos[0]+2] = 1
        except:
            return
        
    def Lblock(self, frame, pos, grid, gameboard = None, orient = 1, gameGridBool = False):
        color = 'blue'
        try:
            if orient == 1:
                if grid != None:
                    frame.itemconfig(grid[pos[1]+1][pos[0]], fill=color)
                    frame.itemconfig(grid[pos[1]+1][pos[0]+1], fill=color)
                    frame.itemconfig(grid[pos[1]+2][pos[0]+1], fill=color)
                    frame.itemconfig(grid[pos[1]+3][pos[0]+1], fill=color)
                if gameGridBool:
                    gameboard[pos[1]+1,pos[0]] = 1
                    gameboard[pos[1]+1,pos[0]+1] = 1
                    gameboard[pos[1]+2,pos[0]+1] = 1
                    gameboard[pos[1]+3,pos[0]+1] = 1
            elif orient == 2:
                if grid != None:
                    frame.itemconfig(grid[pos[1]+3][pos[0]], fill=color)
                    frame.itemconfig(grid[pos[1]+2][pos[0]], fill=color)
                    frame.itemconfig(grid[pos[1]+2][pos[0]+1], fill=color)
                    frame.itemconfig(grid[pos[1]+2][pos[0]+2], fill=color)
                if gameGridBool:
                    gameboard[pos[1]+3,pos[0]] = 1
                    gameboard[pos[1]+2,pos[0]] = 1
                    gameboard[pos[1]+2,pos[0]+1] = 1
                    gameboard[pos[1]+2,pos[0]+2] = 1
            elif orient == 3:
                if grid != None:
                    frame.itemconfig(grid[pos[1]+1][pos[0]+0], fill=color)
                    frame.itemconfig(grid[pos[1]+2][pos[0]+0], fill=color)
                    frame.itemconfig(grid[pos[1]+3][pos[0]+0], fill=color)
                    frame.itemconfig(grid[pos[1]+3][pos[0]+1], fill=color)
                if gameGridBool:
                    gameboard[pos[1]+1,pos[0]+0] = 1
                    gameboard[pos[1]+2,pos[0]+0] = 1
                    gameboard[pos[1]+3,pos[0]+0] = 1
                    gameboard[pos[1]+3,pos[0]+1] = 1
            elif orient == 4:
                if grid != None:
                    frame.itemconfig(grid[pos[1]+3][pos[0]+0], fill=color)
                    frame.itemconfig(grid[pos[1]+3][pos[0]+1], fill=color)
                    frame.itemconfig(grid[pos[1]+3][pos[0]+2], fill=color)
                    frame.itemconfig(grid[pos[1]+2][pos[0]+2], fill=color)
                if gameGridBool:
                    gameboard[pos[1]+3,pos[0]+0] = 1
                    gameboard[pos[1]+3,pos[0]+1] = 1
                    gameboard[pos[1]+3,pos[0]+2] = 1
                    gameboard[pos[1]+2,pos[0]+2] = 1
        except:
            return
        
    def createWidgets(self):
        #Draws the game board.
        self.MainFrame = tk.Canvas(self.main, height = 411, width = 173, bg = 'black') 
        self.MainFrame.place(x = 100, y = 25)
        self.gamegrid = [[0]*10 for i in range(24)]
        self.gamegridnp = np.zeros((24,10)).astype(int)
        s = 500//24-3

        for i in range(24):
            for j in range(10):
                self.gamegrid[i][j] = self.MainFrame.create_rectangle( s*j + 3,s*i+3, s+s*j+3,s+s*i+3, fill = 'white')
        
        #Draws the view window so that we can see what piece the solver is deciding on.
        self.viewWindow = tk.Canvas(self.main, height = 71, width = 71, bg = 'black') 
        self.viewWindow.place(x = 20, y = 25)
        self.viewgrid = [[0]*10 for i in range(24)]

        for i in range(4):
            for j in range(4):
               self.viewgrid[i][j] = self.viewWindow.create_rectangle( s*j + 3,s*i+3, s+s*j+3,s+s*i+3, fill = 'white')    

    def movePossible(self, choice, movchoice):
        #checks to see if the move selected is possible to use.
        self.blockfuncts[choice](self.viewWindow,(0,0), None, gameboard = self.curboard,orient = movchoice[0], gameGridBool=True)
        pos = np.where(self.curboard == 1)
        hasSupport = False #bool to indicated if there's a 1 below block being looked at. If there's at least 1 zero underneath the
        #piece, then this would be set to true. I didn't get this to work.
        for j in range(pos[0].shape[0]):
            y,x = movchoice[1][1]+pos[0][j], movchoice[1][0]+pos[1][j]
            #Makes sure the piece belongs to a spot within the gameboard
            if x > self.gamegridnp.shape[1]-1 or y > self.gamegridnp.shape[0]-1:
                return False
            elif self.gamegridnp[y,x] == 1 and self.curboard[pos[0][j],pos[1][j]] == 1:
                return False
            else:
                #Defaults to a support being true if the block would be placed at the bottom of the gameboard.
                if not y+1 > self.gamegridnp.shape[1]-1:
                    if self.gamegridnp[y+1,x] == 1:
                        hasSupport = True
                else:
                    hasSupport = True
        if not hasSupport:
            return False
        return True
    
    def gameStart(self):
        #Solves for 6 tetris blocks
        for i in range(6):
            #Clears view window
            for k in range(4):
                for j in range(4):
                    self.viewWindow.itemconfig(self.viewgrid[k][j], fill = 'white')
            #Choose a random tetris block to put in the gameboard
            choice = random.randint(0,6)
            #Draw the tetris block into the viewwindow
            self.blockfuncts[choice](self.viewWindow, (0,0), self.viewgrid)
            #Changes the global gamegrid in the prologComp.py program to the gamegrid of this object. (There's probably an 
            #easier way to do this.)
            PC.overWriteGB(self.gamegridnp)
            PC.findFrames(3, [4,4])
            #Output the frame positions and orientations that the ASP solver thought were possible moves
            gameinfo = PC.runProlog(choice)
            #Select a move that follows the game rules.
            while True:
                movChoice = random.randint(0,len(gameinfo)-1)
                if self.movePossible(choice, gameinfo[movChoice]):
                    break
                else:
                    del gameinfo[movChoice]
            self.moves.append([gameinfo[movChoice],choice])
            #finally make the move.
            self.blockfuncts[choice](self.MainFrame, gameinfo[movChoice][1], self.gamegrid, gameboard = self.gamegridnp, orient = gameinfo[movChoice][0], gameGridBool=True)
        #display the moves and the orientations made by the program.
        print(self.moves)
            
#Just means that if this is the program being called, then this block of statements will execute.
if __name__ == "__main__":
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop() 