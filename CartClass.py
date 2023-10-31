# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 09:34:54 2023

@author: ilyes
"""

class Carte:
    def __init__ (self,Nbr,Type,Id):
        self.Id = Id
        self.Nbr =Nbr
        self.Type =Type
        cases ={
            "as":1,
            "deux":2, 
            "trois":3, 
            "quatre":4,
            "cinq":5,
            "six":6, 
            "sept":7, 
            "valet":9,
            "dame":8,
            "roi":10
        }
        self.Power =cases.get(Nbr, 0)
        
    def __str__ (self):
        return f"{self.Nbr}-{self.Type}-#{self.Power} (ID:{self.Id})"
    
    def Copy(self,Nbr,Type):
        CopyObj = Carte()
        CopyObj.Nbr = self.Nbr
        CopyObj.Type =self.Type 
        return CopyObj
    
        
    @staticmethod
    def CopyList(ListOriginalObj):
        ListCopyList=[]
        for orginalObj in ListOriginalObj:
            ListCopyList.append(orginalObj)
        return ListCopyList
        