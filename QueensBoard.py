from typing import List, Set, Dict, Tuple, Optional
import random
class QueensBoard:
    def __init__(self,size:int,autoFill:bool=True):
        self.size:int = size#size of board
        self.board:List[List[int]] = list()#board, 1 = queen 0 = empty
        for i in range(self.size):
            l = list()
            for j in range(self.size):
                l.append(0)
            self.board.append(l)
        if autoFill:
            self.fillRandom()

    def __str__(self):#to string
        re = ""
        for row in self.board:
            rw = "["
            for square in row:
                rw+=str(square)+","
            re += rw[:-1]+"]\n"
        return re

    def getColumn(self,x:int)->List[int]:#returns the column at x
        if not (0<=x<self.size):
            print("invalid location")
            return []
        out:List[int] = list()
        for row in self.board:
            out.append(row[x])
        return out
    
    def getRow(self,y:int)->List[int]:#returns row at y
        if not (0<=y<self.size):
            print("invalid location")
            return []
        return self.board[y]

    def getDiagonals(self,x:int,y:int):#returns 2 lists one of diagonal from up left to down right one from down left to up right
        xtl=(x-y) if (x>=y) else 0
        ytl=(y-x) if (y>=x) else 0
        xbl=(x-((self.size-1)-y)) if (x-((self.size-1)-y))>=0 else 0
        ybl=y+x if y+x<self.size else self.size-1
        re1:List[int]=list()
        re2:List[int]=list()
        tx = xtl
        ty = ytl
        while 0<=tx<self.size and 0<=ty<self.size:
            re1.append(self.board[ty][tx])
            tx+=1
            ty+=1
        tx = xbl
        ty = ybl
        while 0<=tx<self.size and 0<=ty<self.size:
            re2.append(self.board[ty][tx])
            tx+=1
            ty+=-1
        return re1,re2

    def placeQueen(self,x:int,y:int)->bool:#place a queen at coords returns true if success
        if not (0<=x<self.size and 0<=y<self.size):#validate input
            print("invalid coords")
            return False
        if not self.board[y][x]==1:
            self.board[y][x]=1
            return True
        else:
            return False

    def fillRandom(self):
        for i in range(self.size):
            placed = False
            while not placed:
                placed = self.placeQueen(random.randint(0,self.size-1),random.randint(0,self.size-1))

    def swapSquares(self,x1:int,y1:int,x2:int,y2:int)->bool:#swap two squares
        if not (0<=x1<self.size and 0<=y1<self.size):#validate input
            print("invalid coords")
            return False
        if not (0<=x2<self.size and 0<=y2<self.size):#validate input
            print("invalid coords")
            return False
        temp:int
        temp = self.board[y2][x2]
        self.board[y2][x2]=self.board[y1][x1]
        self.board[y1][x1]=temp
        return True

    def numThreats(self,x:int,y:int)->int:#returns the number of queens this tile is threatening
        if not (0<=x<self.size and 0<=y<self.size):#validate input
            print("invalid coords")
            return -1
        offset=self.board[y][x]#used to change our threat value so we dont have to disinclude the spot being checked
        colThreats = sum(self.getColumn(x))-offset
        rowThreats = sum(self.getRow(x))-offset
        d1,d2 = self.getDiagonals(x,y)
        diagThreats1 = sum(d1)-offset
        diagThreats2 = sum(d2)-offset
        threatCount = colThreats+rowThreats+diagThreats1+diagThreats2
        print("offset:",offset,"col",colThreats,"row",rowThreats,"d1",diagThreats1,"d2",diagThreats2,"total",threatCount)
        return threatCount
    