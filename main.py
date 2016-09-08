# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 16:14:11 2016

@author: Fede
"""

"""
IA gana el 98.4+-1 % de las veces y pierde el 0.002+-0.001% 
el de simon que mejora en porcentaje que gana desde ese tablero es 83% y 89%

tablero:
0|1|2
3|4|5
6|7|8
"""

from tatetiextra import Game
from tatetiplayers import Player_random, Player_input,Player_posta


def play(p1,p2,show_board,contar,g1,g2):
    game = Game()
    player = p2
    n=0    
    while not(game.is_draw() or game.anyone_won()) and n<20:
        n+=1
        #print(n)
        
        if player == p1:
            player = p2            
        else:
            player = p1
           
        player.move(game)
        
        if show_board:        
            game.print_Board()
            
    if show_board:     
        if game.is_draw():
            print("empate")
        else:
            print("Gano:",player.name)
    if contar:
        if game.X_won():
            g1+=1
        elif game.O_won():
            g2+=1
            print("si")
    return[g1,g2]
n = 1000
m = 3

    
p3 = Player_random("compu")    
p2 = Player_input("Fede")
p1 = Player_posta("Camelas Benito",n)

g1=0
g3=0
for i in range(n):
    play(p1,p3,False,False,0,0)

for j in range(m):
    [g1,g3]=play(p1,p2,True,True,g1,g3)
    
print("total:",m,"Gano benito:",g1)
