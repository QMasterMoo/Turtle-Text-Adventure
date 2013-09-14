'''
Created on Sep 13, 2013
this is the class for the maze and nothing else.
@author: Dominic
'''
from basicfunc import *

class maze:
    '''
    classdocs
    '''



    def __init__(self, name):
        '''
        Constructor
        
        '''
        self.name = name
    

    def mazeWelcome(self):      #Just a simple welcome message to be called from the main TTA file.
        print "Welcome to the maze of HerpaDerp, ", self.name
        print " "
        print "Good luck."
        '''
        This method is the core of the class
        it creates the maze
        '''
    def doMaze(self):
        self.mazeArr = [['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','e','w','w','w','w','w',]
                        ['w','p','w','p','p','p','p','p','p','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','p','w','w','w','w','w',]
                        ['w','p','w','p','w','w','w','w','p','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','p','w','w','w','w','w',]
                        ['w','p','w','p','w','p','p','p','p','w','w','w','w','w','w','w','w','p','p','p','p','p','p','p','p','w','w','w','w','w',]
                        ['w','p','p','p','w','p','w','w','w','w','w','w','w','w','w','w','w','p','w','w','w','w','w','w','w','w','w','w','w','w',]
                        ['w','w','w','w','w','p','w','w','w','w','w','w','w','w','w','w','w','p','w','w','w','w','w','w','w','w','w','w','w','w',]
                        ['w','p','p','p','p','p','w','w','w','w','w','w','w','w','w','w','w','p','w','w','w','w','w','w','w','w','w','w','w','w',]
                        ['w','p','w','w','w','w','w','w','w','w','w','w','w','w','w','w','p','p','w','w','w','w','w','w','w','w','w','w','w','w',]
                        ['w','p','p','w','p','p','p','w','w','w','w','w','w','w','p','p','p','w','w','w','w','w','w','w','w','w','w','w','w','w',]
                        ['w','p','w','w','p','w','p','w','w','w','w','w','w','w','p','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w',]
                        ['w','p','p','w','p','w','p','w','w','w','w','w','w','w','p','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w',]
                        ['w','p','w','w','p','w','p','w','w','w','w','w','w','w','p','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w',]
                        ['w','p','p','w','p','w','p','w','w','w','w','w','w','w','p','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w',]
                        ['w','p','w','w','p','w','p','w','w','p','p','p','p','p','p','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w',]
                        ['w','p','p','w','p','w','p','w','w','w','p','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w',]
                        ['w','p','w','w','p','w','p','w','w','w','p','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w',]
                        ['w','p','p','w','p','w','p','w','w','w','p','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w',]
                        ['w','p','w','w','p','w','p','w','w','w','p','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w',]
                        ['w','p','p','w','p','w','p','w','w','w','p','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w',]
                        ['w','p','w','w','p','w','p','w','w','w','p','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w',]
                        ['w','p','p','w','p','w','p','w','w','w','p','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w',]
                        ['w','p','w','w','p','w','p','w','w','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','p','w',]
                        ['w','p','p','w','p','w','p','p','w','p','w','p','w','w','w','w','w','w','w','w','w','w','w','p','w','w','w','w','p','w',]
                        ['w','p','w','w','p','w','w','p','w','p','w','p','w','w','w','w','w','w','w','w','w','w','w','p','p','w','w','w','p','w',]
                        ['w','p','p','w','p','p','w','p','w','p','w','p','w','w','w','w','w','w','w','p','p','p','p','p','p','p','p','w','p','w',]
                        ['w','p','w','w','w','p','w','p','w','p','w','p','w','w','w','w','w','w','w','p','w','w','w','w','p','w','p','w','p','w',]
                        ['w','p','p','p','p','p','w','p','w','p','p','p','p','p','p','p','p','p','w','p','w','w','w','w','p','w','p','w','p','w',]
                        ['w','p','w','w','w','w','w','p','w','w','p','w','w','w','w','w','w','p','w','p','w','w','w','w','p','w','p','w','p','w',]
                        ['w','p','p','p','w','w','w','p','w','w','p','w','w','w','w','w','w','p','w','p','w','w','w','w','p','w','p','w','p','w',]
                        ['w','p','w','p','w','w','w','p','p','w','p','w','w','w','w','w','w','p','w','p','p','p','p','p','p','w','p','w','p','w',]
                        ['w','p','p','p','w','w','w','w','p','w','p','w','w','w','w','w','p','p','w','w','w','w','w','w','w','w','p','p','p','w',]
                        ['w','p','w','w','w','w','w','w','p','p','p','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w',]
                        ['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w',]]
        

    def printMaze(self):
        for 
    
    
    
    def wayOut(self, r, c):
        self.r = 1
        self.c = 1
        


        location = self.mazeArr[[r][c]]
        
        #Core movement function
        while not 'e':
            print " "
            move = raw_input("Which way would you like to proceed? (Up, Down, Left, Right)")
            stringit(move)
            lowerit(move)
            
            if move == "down":
                if self.mazeArr[[r+1][c]] == 'w':
                    print" "
                    print "There is a wall in front of you."
                    break
                else: location = self.mazeArr[[r+1]]
                
                
                
            
    
        
        
        
        
        
        