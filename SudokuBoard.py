from typing import List, Set, Dict, Tuple, Optional
import copy
import random
import csv
class SudokuBoard:
    
    def __init__(self,fileName:str="",autofill:bool=True):
        self.completeSet:Set[int]=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
        self.size=25
        self.board=list()
        self.lockedSquares=list()
        for i in range(self.size):
                l = list()
                for j in range(self.size):
                    l.append(0)
                self.board.append(l)
        if fileName!="":
            self.populate(fileName)
        if autofill:
            self.fillAll()

    def populate(self,fileName:str):
        with open(fileName) as csvfile:
            reader = csv.reader(csvfile)
            rw = 0
            for row in reader:
                col = 0
                for val in row:
                    self.board[rw][col]=int(val)
                    col+=1
                rw+=1
        self.lockedSquares=copy.deepcopy(self.board)
        for y,row in enumerate(self.lockedSquares):
            for x,val in enumerate(row):
                self.lockedSquares[y][x]=True if val!=0 else False

    def __str__(self):#to string
        re = ""
        for y,row in enumerate(self.board):
            rw = "["
            for x,square in enumerate(row):
                rw+=str(square).zfill(2)+ ("," if not (x+1)%5==0 else "|")
            re += rw[:-1]+"]\n"
            if (y+1)%5 ==0 and not y==24:
                re+="---------------------------------------------------\n"

        return re

    def __getitem__(self,key):#make board subscriptable i.e. qb[2][1]
        return self.board[key]
        
    def getColumn(self,x:int)->List[int]:#returns the column at x
        if not (0<=x<self.size):
            print("invalid location")
            return []
        out:List[int] = list()
        for row in self.board:
            out.append(row[x])
        return out

    def fillAll(self):
        for i in range(5):
            for j in range(5):
                self.fillRegion(i,j)
                
    def getRow(self,y:int)->List[int]:#returns row at y
        if not (0<=y<self.size):
            print("invalid location")
            return []
        return self.board[y]
    
    def getRegion(self,x:int,y:int)->List[List[int]]:#returns a region as a 2d array
        x = x*5
        y = y*5
        re:List[List[int]] = list()
        for row in range(5):
            l=list()
            for column in range(5):
                l.append(self.board[y+row][x+column])
            re.append(l)
        return re
    def setRegion(self,x:int,y:int,ls:List[List[int]]):
        x = x*5
        y = y*5
        for row in range(5):
            for column in range(5):
                if not self.lockedSquares[y+row][x+column]:
                    self.board[y+row][x+column]=ls[row][column]
                else:
                    print("lock")
        
    
    def fillRegion(self,x:int,y:int):
        l=list()
        rg = self.getRegion(x,y)
        for row in rg:
            for element in row:
                if not element==0:
                    l.append(element)
        remaining = list(set(self.completeSet)-set(l))
        print(remaining)
        random.shuffle(remaining)
        for yy,row in enumerate(rg):
            for xx,val in enumerate(row):
                if rg[yy][xx]==0:
                    print(remaining)
                    rg[yy][xx]=remaining.pop()
        print(rg)    
        self.setRegion(x,y,rg)
