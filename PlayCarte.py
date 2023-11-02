# -*- coding: utf-8 -*-

import random 
from  CartClass import Carte
import functions 
from  GameCartEvaluationClass import Evaluation

def Shuffle(carts):
    shuffledCarts =[""] * len(carts)
    for item in carts:
        index =0
        while(shuffledCarts[index]!=""):
            index = random.randint(0, len(carts)-1)
        shuffledCarts[index]=item
    return shuffledCarts
def Tire(AllCarts,Playr1Carts,Player2Carts):
    print("\nTirage...")
    i=0;
    TIRE_FOR_1_PLAYER = 3
    for i in range(0,TIRE_FOR_1_PLAYER):
            Playr1Carts.append(AllCarts[0])   
            del  AllCarts[0]
            Player2Carts.append(AllCarts[0]) 
            del  AllCarts[0]
    return {"ALL":AllCarts,"1": Playr1Carts,"2" :Player2Carts}
def GetCartForTable(AllCarts):
    i=0;
    CartsForTable= []
    for index in range(0,4):
        CartsForTable.append(AllCarts[index])
        del  AllCarts[index]
    return {"ALL":AllCarts,"TABLE": CartsForTable}   
def PrintCarts(carts,texttoPrint):
    print(f"\n{texttoPrint} :",end="")
    for item in carts:
        print(f"{item}", end=' | ')
def GetCartById(listCart,cartId):
    for item in listCart:
        if(int(item.Id) == int(cartId)):
            return item        
def CanHeEatChoosenCarts(pickedCart,ListCartsToEat):
    sumPowerOfToEatCart =0
    if(pickedCart!=None and ListCartsToEat!=[None]):
        for item in ListCartsToEat:
            sumPowerOfToEatCart=sumPowerOfToEatCart+item.Power
        if(sumPowerOfToEatCart==pickedCart.Power):
            return True
    return False
def EatCarts(cartsForTable,carts_player,winnings_player,pickedCart,ListCartsToEat):
    winnings_player.append(pickedCart)
    winnings_player+=ListCartsToEat
    for item in ListCartsToEat:
        cartsForTable.remove(item)
    carts_player.remove(pickedCart)
    return {"TABLE":cartsForTable,"CARTS_PLAYER": carts_player,"WINNINGS":winnings_player}
def OnePlayerTour(cartsForTable,carts_player,winnings_player,PlayerName):
    PickedCartId = functions.GetOnlyIntInput(f"{PlayerName}- picker une carte (par ID)")
    PickedCart = GetCartById(carts_player,PickedCartId)
    while(PickedCart==None):
        PickedCartId = functions.GetOnlyIntInput(f"---Id n'existe pas!---{PlayerName}- picker une carte (par ID)")
        PickedCart = GetCartById(carts_player,PickedCartId)
        
    CartsIdToEat_str = input(f"{PlayerName}- choisir les cartes a monger separe par vergule (par ID) :")
    if(CartsIdToEat_str!=''):
        ListCartsIdToEat =CartsIdToEat_str.split(",")
        ListCartsToEat =[]
        for item in ListCartsIdToEat:
            ListCartsToEat.append(GetCartById(cartsForTable,item))
        isCanEat = CanHeEatChoosenCarts(PickedCart,ListCartsToEat)
        if(isCanEat==True):
            result = EatCarts(cartsForTable,carts_player,winnings_player,PickedCart,ListCartsToEat)
            cartsForTable=result["TABLE"]
            carts_player=result["CARTS_PLAYER"]
            winnings_player=result["WINNINGS"]
            return {"TABLE":cartsForTable,"CARTS_PLAYER": carts_player,"WINNINGS":winnings_player,"ISEATED":True}
    cartsForTable.append(PickedCart)
    carts_player.remove(PickedCart)
    return {"TABLE":cartsForTable,"CARTS_PLAYER": carts_player,"WINNINGS":winnings_player,"ISEATED":False} 
def AssignChkobaIfExisit(cartsForTable):
    chkoba =0
    if(len(cartsForTable)==0):
        chkoba=1
        print("**********************ChHkObBbBbAaAaAaAaaA")
    return chkoba
def PlayATour(Game):
    

    PrintCarts(Game.carts_player1,"Carte J1")
    PrintCarts(Game.cartsForTable,"[--] Carte sur table")
    # player 1 tour
    result = OnePlayerTour(Game.cartsForTable,Game.carts_player1,Game.winnings_player1,"J1")
    Game.cartsForTable=result["TABLE"]
    Game.carts_player1=result["CARTS_PLAYER"]
    Game.winnings_player1=result["WINNINGS"]
    isP1Eated =result["ISEATED"]
    if(isP1Eated==True):
        Game.lastEatedPlayer=1
        # assign chkoba exisit for player1
    Game.EvaluationPlayer1.NbrChkobas= AssignChkobaIfExisit(Game.cartsForTable)
    # player 1 tour
    PrintCarts(Game.carts_player2,"Carte J2")
    PrintCarts(Game.cartsForTable,"[--] Carte sur table")
    result = OnePlayerTour(Game.cartsForTable,Game.carts_player2,Game.winnings_player2,"J2")
    Game.cartsForTable=result["TABLE"]
    Game.carts_player2=result["CARTS_PLAYER"]
    Game.winnings_player2=result["WINNINGS"]
    isP2Eated =result["ISEATED"]
    if(isP2Eated==True):
        Game.lastEatedPlayer=2
        # assign chkoba exisit for player1
    Game.EvaluationPlayer2.NbrChkobas= AssignChkobaIfExisit(Game.cartsForTable)
    return Game
def LastEatedTakeAllCartsOnTable(Game):
    if(len(Game.cartsForTable)>0):
        if(Game.lastEatedPlayer ==1):
            Game.winnings_player1+=Game.cartsForTable
        elif(Game.lastEatedPlayer ==2):
            Game.winnings_player2+=Game.cartsForTable
    return Game
def Evaluation(Game):
    scoreP1=0
    scoreP2=0
    PrintCarts(Game.winnings_player1,"********[Les cartes Gagants J1]")    
    PrintCarts(Game.winnings_player2,"********[Les cartes Gagants J2]")
    # nbr carts
    Game.EvaluationPlayer1.NbrCarts=len(Game.winnings_player1)
    Game.EvaluationPlayer2.NbrCarts=len(Game.winnings_player2)
    # septCareau
    for item in Game.winnings_player1:
        if(item.Nbr == "sept" and item.Type=="careau"):
            Game.EvaluationPlayer1.septCareau=True
            # continue COUNTING SCORE
            scoreP1+=1
            
    if(Game.EvaluationPlayer1.septCareau==False):
        for item in Game.winnings_player2:
            if(item.Nbr == "sept" and item.Type=="careau"):
                Game.EvaluationPlayer2.septCareau=True
                # continue COUNTING SCORE
                scoreP2+=1
    #7s 
    for item in Game.winnings_player1:
        if(item.Nbr == "sept"):
            Game.EvaluationPlayer1.Nbr7s+=1
    for item in Game.winnings_player2:
        if(item.Nbr == "sept"):
            Game.EvaluationPlayer2.Nbr7s+=1
    # 6s
    for item in Game.winnings_player1:
        if(item.Nbr == "six"):
            Game.EvaluationPlayer1.Nbr6s+=1
    for item in Game.winnings_player2:
        if(item.Nbr == "six"):
            Game.EvaluationPlayer2.Nbr6s+=1    
            
    # continue COUNTING SCORE
    if(len(Game.winnings_player1)>len(Game.winnings_player2)):
        scoreP1+=1
    else:
        scoreP2+=1
    if(Game.EvaluationPlayer1.Nbr7s >Game.EvaluationPlayer2.Nbr7s):
        scoreP1+=1
    elif(Game.EvaluationPlayer1.Nbr7s <Game.EvaluationPlayer2.Nbr7s):
        scoreP2+=1
    else:
        if(Game.EvaluationPlayer1.Nbr6s >Game.EvaluationPlayer2.Nbr6s):
            scoreP1+=1
        elif(Game.EvaluationPlayer1.Nbr6s <Game.EvaluationPlayer2.Nbr6s):
            scoreP2+=1
    scoreP1+=Game.EvaluationPlayer1.NbrChkobas
    scoreP2+=Game.EvaluationPlayer2.NbrChkobas
    print(f"\n[...Analayse J1 ] = Cartes: {Game.EvaluationPlayer1.NbrCarts}/cept-careau : {Game.EvaluationPlayer1.septCareau} /les 7 : {Game.EvaluationPlayer1.Nbr7s}/les 6 : {Game.EvaluationPlayer1.Nbr6s} /Chkobas :{Game.EvaluationPlayer1.NbrChkobas}")
    print(f"\n[...Analayse J2 ] = Cartes: {Game.EvaluationPlayer2.NbrCarts}/cept-careau : {Game.EvaluationPlayer2.septCareau} /les 7 : {Game.EvaluationPlayer2.Nbr7s}/les 6 : {Game.EvaluationPlayer2.Nbr6s}/Chkobas :{Game.EvaluationPlayer2.NbrChkobas}")
    
    print(f"\nScore J1 : {scoreP1}")
    print(f"\nScore J2 : {scoreP2}")
    print(f"\nle Gagnant est...")
    winner =""
    if(scoreP1>scoreP2):
        winner="J1"
    else:
        winner="J2"
    print(f"\n{winner}")
    
        
            
        
        
    
        
        