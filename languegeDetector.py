#!/usr/bin/python
#-*- coding: utf-8 -*-

## coder par G33ke n30 
## language python 3.12.X
## licence : GNU free 
## version du code 


#importation des modules utilisé
import os, time
from frequency import *



## classe des detection de la langues

class LanguageDetect:

    def __init__(self):
        self.alpha = [lttr for lttr in "abcdefghijklmnopqrstuvwxyz"]

    
    def aproxiNbr(self, fix: float, dpsmnt: float, fq_vl:float) -> bool:

        self.fix = fix
        self.dpsmt_pxi = dpsmnt
        self.fq_vl = fq_vl
        
        self.express = (self.fq_vl + self.dpsmt_pxi) > self.fix

        if (((self.fix - self.fq_vl) <= self.fq_vl) and ( self.dpsmt_pxi <= (self.fix + self.dpsmt_pxi))):
                return True
        else:
            return False
        
    def frequency(self, wrds):
        self.wrds = words
        self.occur = {}
        self.l_occur_prctg = {}
        for l in self.alpha: 
            self.occur[l] = self.wrds.count(l)

        for key, value in self.occur.items():
            self.l_occur_prctg[key] = round((100 * value / 26),1)

        return self.l_occur_prctg



              

# test 

if __name__ == "__main__":
    print("="*50)
    print("programme de tetection de langue".upper())
    print("="*50)
    
    words = input("Entre la phrase: _ ")
    lD = LanguageDetect()
    # fr_ltrs_frq["E"], 5.6, 23.78
    frqnc = lD.frequency(words)

    for k, v in frqnc.items():
        print(f"{k} = {v}")
    # vls = [v+v for v in frqnc.values]
    print("==========================================")
    vls = 0
    print(f"all value % = {vls}")





     