# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 16:14:11 2016

@author: Fede
"""
import random
from tatetilist import Lista, Nodo
from tatetilist import generate_values
from tatetiextra import Game



#######################################################

class Player_random:
    def __init__(self,name):
        self.name = name
        
    def move(self,game):
        n = random.randrange(9)
        while not(game.valid_move(n)):
            n = random.randrange(9)
        game.make_move(n)

#######################################################

class Player_input:
    def __init__(self,name):
        self.name = name
        print(" Tablero:")
        print("  0|1|2")        
        print("  3|4|5")        
        print("  6|7|8")        
        
    def move(self,game):
        n = int(input("ingrese movimiento:"))
        while not(game.valid_move(n)):
            print("la posicion ingresada no es valida, intente de nuevo")
            n = int(input("ingrese movimiento:"))
        game.make_move(n)
    
  

######################################################

#backtracking auxiliary function:
def aux_armar(symbols, board_size, possible_board,lista):
    if len(possible_board)== board_size:
        lista.add_node(possible_board)
    else:
        for element in symbols:
            possible_board.append(element)
            aux_armar(symbols, board_size,possible_board,lista)
            possible_board.pop(len(possible_board)-1)

def armar(lista):
    symbols  = [0,"X","O"]
    board_size = 9                                                             
    possible_board = []
    aux_armar(symbols, board_size, possible_board,lista)
        
        
class Player_posta:
    def __init__(self,name,numero_entrenamientos):
        self.name = name
        self.num = numero_entrenamientos
        lista = Lista()     
        armar(lista)
        self.memoria = lista
        self.tableros_jugados = []
        
    def movimientos(self):
        return self.memoria
        
    def move(self,game):
        if game.squares == [0]*9:
            self.tableros_jugados = [] 
        
        self.tableros_jugados.append(game.squares[:])
        posibles_moves = game.possible_moves()            
        posibles_values = []
        for move in posibles_moves:
            game.make_move(move)
            posibles_values.append(self.memoria.find_node(game.squares).value)
            game.unmake_move(move)
            
        n = random.randint(0,100)
        if self.num<100:
            m = 81        
        else:
            m = 0
        if n<m:    
            move = posibles_moves[ n % len(posibles_moves) ]
        else:
            move = posibles_moves[posibles_values.index(max(posibles_values))]
    
        game.make_move(move)
        self.tableros_jugados.append(game.squares[:])
        
        
        if game.X_won():                                                       # es X
            self.modify_values(1)
        elif game.going_to_lose()[0]:
            self.tableros_jugados.append( game.going_to_lose()[1])
            self.modify_values(0)
            
    def modify_values(self,i):    
        value2 = i
        for tablero in self.tableros_jugados:
            value1 = self.memoria.find_node(tablero).value
            alfa = 0.9
            value1 = value1 + alfa * ( value2 - value1)
            self.memoria.find_node(tablero).value = value1
        
        
        
######################################################
