from typing import List, Set, Dict, Tuple, Optional
import random
import csv
class SudokuBoard:
    def __init__(self,fileName:str=""):
        self.size=25
        self.board=list()
        for i in range(self.size):
                l = list()
                for j in range(self.size):
                    l.append(0)
                self.board.append(l)
        if fileName!="":
            self.populate(fileName)
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
    def __str__(self):#to string
        re = ""
        for row in self.board:
            rw = "["
            for square in row:
                rw+=str(square)+","
            re += rw[:-1]+"]\n"
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
    
    def getRow(self,y:int)->List[int]:#returns row at y
        if not (0<=y<self.size):
            print("invalid location")
            return []
        return self.board[y]
