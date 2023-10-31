# -*- coding: utf-8 -*-
import random
from GameCarteClass import GameCarte
from  CartClass import Carte
import PlayCarte



# main

Game = GameCarte()
idCart=1
for cartNbr in ["as", "deux", "trois", "quatre", "cinq", "six", "sept", "valet", "dame", "roi"]:
    for cartType in ["cœur", "pique", "carreau","trèfle"]:
        CarteObj  = Carte(cartNbr,cartType,idCart)
        Game.carts.append(CarteObj)
        idCart+=1
        
        

PlayCarte.PrintCarts(Game.carts,"tous")

print(f"\nmelange...")
Game.carts = PlayCarte.Shuffle(Game.carts)
PlayCarte.PrintCarts(Game.carts,"tous les Cartes mixé")

result = PlayCarte.GetCartForTable(Game.carts)
Game.carts = result["ALL"]
Game.cartsForTable=result["TABLE"]
while(len(Game.carts)!=0):
   
    result = PlayCarte.Tire(Game.carts,Game.carts_player1,Game.carts_player2)
    carts = result["ALL"]
    Game.carts_player1=result["1"]
    Game.carts_player2=result["2"]
    print(f"\nTous Carte({len(Game.carts)})")
    while(len(Game.carts_player1)>0 or len(Game.carts_player2)>0):
        Game = PlayCarte.PlayATour(Game)

Game =PlayCarte.LastEatedTakeAllCartsOnTable(Game)
PlayCarte.PrintCarts(Game.winnings_player1,"Carte gagne par J1")
PlayCarte.PrintCarts(Game.winnings_player2,"Carte gagne par J2")
PlayCarte.Evaluation(Game)


