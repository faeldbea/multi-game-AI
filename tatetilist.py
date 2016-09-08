# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 01:09:53 2016

@author: Fede
"""
#el orden en la lista esta prefijado
from tatetiextra import Game



def generate_values(game):
    if game.O_won():
        RV = 0
    elif game.X_won():
        RV = 1
    else:
        RV = 0.5
    return RV
    
class Nodo:
    def __init__(self,game,value):
        self.hijos = [None,None,None]  # 0,"X","O"
        self.value = value
        self.game = game
        
    def change_value(self,new_value):
        self.value = new_value
        
        
        
        
        
class Lista:
    def __init__(self):        
       n = Nodo(Game(),0.5)
       n.game.squares = [None, None, None, None, None, None, None, None, None]
       self.primero = n
       
    def add_node(self,board):
        board_size = len(board)
        n = self.primero
        tablero_parcial = [None, None, None, None, None, None, None, None, None]
        
        for i in range(board_size):
            tablero_parcial[i] = board[i]
            hijo_a_ver = 0 if board[i]==0 else 1 if board[i]=="X" else 2
            if n.hijos[hijo_a_ver]==None:
                nuevo_nodo = Nodo(Game(),0.5)         
                nuevo_nodo.game.squares = tablero_parcial
                n.hijos[hijo_a_ver] = nuevo_nodo
                n = nuevo_nodo
            else:
                n = n.hijos[hijo_a_ver]
        n.value = generate_values(n.game)
        
    def find_node(self, board):
        board_size = len(board)
        node = self.primero 
        for i in range(board_size):
            hijo_a_ver = 0 if board[i]==0 else 1 if board[i]=="X" else 2
            node = node.hijos[hijo_a_ver]
        return node
     
     
  
     
