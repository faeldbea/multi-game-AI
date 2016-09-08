# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

"""
tablero:
0|1|2
3|4|5
6|7|8
"""


class Game:
    def __init__(self):        
        self.squares = [0,0,0,0,0,0,0,0,0]
        self.turn = "X"       
        
    def print_Board(self):
        print("")
        print(self.squares[:3])
        print(self.squares[3:6])
        print(self.squares[6:])
        print("")
        
    def __str__(self):
        return str(self.squares)
        
    def switch_turn(self):
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"
            
            
    def X_won(self):
        RV = False
        if self.squares[0]==self.squares[4]==self.squares[8]=="X" :
            RV = True
        elif  self.squares[2]==self.squares[4]==self.squares[6]=="X":
            RV = True
            
        elif  self.squares[0]==self.squares[1]==self.squares[2]=="X":
            RV = True
        elif  self.squares[3]==self.squares[4]==self.squares[5]=="X":
            RV = True
        elif  self.squares[6]==self.squares[7]==self.squares[8]=="X":
            RV = True
            
        elif  self.squares[0]==self.squares[3]==self.squares[6]=="X":
            RV = True
        elif  self.squares[1]==self.squares[4]==self.squares[7]=="X":
            RV = True
        elif  self.squares[2]==self.squares[5]==self.squares[8]=="X":
            RV = True
            
        return RV

    def O_won(self):
        RV = False
        if self.squares[0]==self.squares[4]==self.squares[8]=="O" :
            RV = True
        elif  self.squares[2]==self.squares[4]==self.squares[6]=="O":
            RV = True
            
        elif  self.squares[0]==self.squares[1]==self.squares[2]=="O":
            RV = True
        elif  self.squares[3]==self.squares[4]==self.squares[5]=="O":
            RV = True
        elif  self.squares[6]==self.squares[7]==self.squares[8]=="O":
            RV = True
            
        elif  self.squares[0]==self.squares[3]==self.squares[6]=="O":
            RV = True
        elif  self.squares[1]==self.squares[4]==self.squares[7]=="O":
            RV = True
        elif  self.squares[2]==self.squares[5]==self.squares[8]=="O":
            RV = True
            
        return RV

    def anyone_won(self):
        return self.O_won() or self.X_won()
        

    def is_draw(self):
        RV = False        
        if not(0 in self.squares) and not(self.anyone_won()):
            RV = True            
        return RV

    def valid_move(self,move):
        if self.squares[move] == 0:
            RV = True
        else:
            RV = False
        return RV
    
    def possible_moves(self):
        l = [0,1,2,3,4,5,6,7,8]            
        for i in range(9):
            if not(self.valid_move(i)):
                l.remove(i)
        return l
        
    def make_move(self,move):
        if self.valid_move(move):
            self.squares[move] = self.turn
            self.switch_turn()
        else:
            print("Error")
        
    def unmake_move(self,move):
        self.squares[move] = 0
        self.switch_turn()
        
    def going_to_lose(self):
        RV1=False
        RV2=None
        for move in self.possible_moves():
            self.make_move(move)
            if self.O_won():
                RV1 = True
                RV2 = self.squares[:]
            self.unmake_move(move)
     
        return [RV1,RV2]

##############################################
