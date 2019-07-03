import os
import numpy as np
import random

#Necessary instantiations

#Each of these pieces do practically the same thing. I formatted the code such that it's easy to see the array representation
#that's being looked at.
piecesEnum = ['Opiece.lp', 'Ipiece.lp', 'Spiece.lp', 'Zpiece.lp','Lpiece.lp','Jpiece.lp', 'Tpiece.lp']
global frames,gameboard, curdir, gameboarddims
frames,gameboarddims = [],[]
curdir = os.path.dirname(os.path.realpath(__file__))
#Instantiates a 24x10 numpy array of zeros which the values are integers.
gameboard = np.zeros((24,10)).astype(int)

#Class frame which holds the position and the frame that corresponds with it.
class Frame:
    def __init__(self, pos, frame):
        self.pos = pos
        self.frame = frame

def writeFramesinProlog():
    file = open(curdir+'\\lp codes\\data.lp','w')
    counter = 1
    #Write the data or frames into data.lp.
    for frame in frames:
        frame = frame.frame
        strWrite = 'frame('
        for i in range(frame.shape[0]):
            strWrite += str(counter)+','+str(i)+','+str(frame[i,0])+','+str(frame[i,1])+','+str(frame[i,2])+','+str(frame[i,3])
            if i < frame.shape[0]-1:
                strWrite += ';'
            else:
                strWrite += ').'
        counter += 1
        file.write(strWrite+'\n')
    file.close()

def runProlog(pieceEnum):
    writeFramesinProlog()
    os.chdir(curdir+"\\lp codes")
    #Select the logic program file that corresponds with the piece chosen.
    os.system('clingo data.lp pieces\\'+ piecesEnum[pieceEnum] +' > output.lp')

    file = open('output.lp', 'r')
    prolog_output = file.readlines()[4]
    file.close()
    #parse output.
    posors = parseOutput(prolog_output)
    posmovs = []
    for posor in posors:
        #Return the orientation in posor[0] and return the position in frame, which is found at index posor[1]
        posmovs.append([posor[0],frames[posor[1]].pos])
    #return the formatted outputs.
    return posmovs 

def parseOutput(prolog_output):
    info = []
    while True:
        try:
            posStart = prolog_output.find('sframe')
            abbrev = prolog_output[posStart:]
            posEnd = abbrev.find(')')
            abbrev = abbrev[:posEnd].split('t')[1].split(',')
            prolog_output = prolog_output[posStart + posEnd:]
            info.append([int(abbrev[0]),int(abbrev[1])-1])
        except:
            break
    return info

def findFrames(padding, dim):
    #Find possible locations where the tetris blocks could go, otherwise known as the frames.
    global gameboarddims, frames
    frames = []
    gameboarddims = [gameboard.shape[0]+padding,gameboard.shape[1]+padding]
    paddedGB = np.zeros((gameboarddims[0],gameboarddims[1])).astype(int)
    paddedGB[padding:paddedGB.shape[0],:paddedGB.shape[1]-padding] = gameboard 
    for i in range(paddedGB.shape[1]-padding):
        ones = np.where(paddedGB[:,i] == 1)
        endPoints = []
        frame = []
        #If no ones were found on a column of the numpy array's gamegrid, then we make a frame that begins 4 up from the bottom,
        #and i from the left.
        if ones[0].size == 0:
                endPoints = [i, paddedGB.shape[0] - dim[1] - padding,i+dim[0], paddedGB.shape[0]-padding]
                frame = paddedGB[endPoints[1]:endPoints[3],endPoints[0]:endPoints[2]]
                frame = Frame((endPoints[0],endPoints[1]),frame)
                frames.append(frame)
        else:
            #If there are more than one 1s in the column, go through all of them and make frames.
            for num in ones:
                endPoints = [i, num[0]-dim[1],i+dim[0], num[0]]
                frame = paddedGB[endPoints[1]:endPoints[3],endPoints[0]:endPoints[2]]
                endPoints = [endPoints[0],endPoints[1] - padding]
                frame = Frame((endPoints[0],endPoints[1]),frame)
                frames.append(frame)

                endPoints = [i, num[0]-dim[1]+1,i+dim[0]+1, num[0]]
                frame = paddedGB[endPoints[1]:endPoints[3],endPoints[0]:endPoints[2]]
                endPoints = [endPoints[0],endPoints[1] - padding]
                if frame.shape[0] == 4:
                    frame = Frame((endPoints[0],endPoints[1]),frame)
                    frames.append(frame)
        #these frames are used to be analyzed by the ASP program.

def overWriteGB(curgame):
    global gameboard
    gameboard = curgame

#This is here for test purposes.
if __name__ == "__main__":
    choice = random.randint(1,7)
    findFrames(3, [4,4])
    prolog_output = runProlog(6)
    print(choice)
    print(prolog_output)