#!/usr/bin/python
#-*- coding: utf-8 -*-

## coder par G33ke n30 
## language python 3.12.X
## licence : GNU free 
## version du code 


#importation des modules utilisé
import os, time, sys
from frequency import *



## classe des detection de la langues

class LanguageDetect:
    """
    class: LanguageDect :
        methode:
            ** aproxiNbr (methode recherche de valeur aproximative):
                paramettre :
                    fix: type float (variable de du nombre fix)
                    dpsmnt : type float (variable de dépénsement d'aproximatiion)
                    fq_vl : type float (variable valuer du fréquence réchercher)
                return :
                    boolear True or False
                    
            ** frequency: (Methode de calcule de fréquence)
                paramettre:
                    words: type str (variable de la phases)
                return:
                    list() (liste d'de pourçantage d'occurence des chaque mot dans l'alphabet)
    """

    def __init__(self):
        self.alpha = [lttr for lttr in "abcdefghijklmnopqrstuvwxyz"]

    
    def _aproxiNbr(self, fix: float, dpsmnt: float, fq_vl:float) -> bool:
        """la méthode de recherche d'une valeur approximative

        Args:
            fix (float): la valeur fixe qu'on recherche son appriximation
            dpsmnt (float): le nombre de dépassement de la valeur de l'apprimité
            fq_vl (float): la valeur en fréquence de la lettre 

        Returns:
            bool: La valeur Booleen si fq_vl et vrais ou fausse
        """
        self.fix = fix
        self.dpsmt_pxi = dpsmnt
        self.fq_vl = fq_vl
        
        self.express = (self.fq_vl + self.dpsmt_pxi) > self.fix

        if (((self.fix - self.fq_vl) <= self.fq_vl) and ( self.dpsmt_pxi <= (self.fix + self.dpsmt_pxi))):
                return "True"
        else:
            return "False"

    
    def frequency(self, wrds: str) -> dict:
        """Méthode de calcule de fréquence d'apparrution de lettre dans l'alphabet fr ou en

        Args:
            wrds (string): Les textes du test de detection de la langue

        Returns:
            dict: Retourn d'un dictionnaire contenant l'occurent en fréquence de chaque lettre de l'alphabet
        """
        self.wrds = wrds
        self.occur = {}
        self.l_occur_prctg = {}
        for l in self.alpha: 
            self.occur[l] = self.wrds.count(l)

        for key, value in self.occur.items():
            self.l_occur_prctg[key] = round((100 * value / 26),1)

        return self.l_occur_prctg
    
    

    def detectLanguage(self, wrds_frqncs: dict) -> str:
        """fonction principale de detection du langue

        Args:
            wrds_frqncs (dict): l'association de fréquence et leurs valeurs en % d'occurence

        Returns:
            str: return la langue trouvé
        """
        self.wrds_frqncs = wrds_frqncs
        languages = ["fr", "en"]
        self.fr_crpus = {}
        lg_rounded = ""
        print("Test 0")
        ## checking all letters and th
        
        
        for l in self.wrds_frqncs.keys():
            print(f"{l} = {self.wrds_frqncs[l]}")




################################################
# Fonction du gestion du fichier


help = """
    veuillez utiliser le fichier comme ceci:
        languegeDetector.py [-f][-v]
        -f == for file name
        -v == show script version

    Syntax: languageDetector.py -f file.txt
            languageDetector.py -v
            
"""
def fileManager():
    out_put_f_content = ""
    all_args = sys.argv


    print("Test 1")
    
    if len(all_args) < 3:
        if all_args[1] == "-h": # renvoie le help si pour le l'argument -h
            return help
            
        if len(all_args) == 1:
            return  "-- Il  manque  les arguments du fichier | type : languageDetector.py -h for help  --"
        else:
            return "-- Syntax to open file error -- | type : languageDetector.py -h for help"
        
    else:
        if all_args[1].lower() == "-h":
            return help
        elif all_args[1].lower() == "-v":
            return "Script version : 0.1 python3.x"
        elif all_args[1].lower() == "-f":
            f_name = all_args[2].lower()

            with open(f_name) as f_n:
                for i in f_n:
                    if i == "\n":
                        pass
                    else:
                        print("Test 5")
                        out_put_f_content += i
        return   out_put_f_content
        
    

## comparaison of corpus with letter

def frCorpusDector(lttr: str, value: float) -> bool:
    if lttr in list(fr_coprus_wk.keys()):
        print("True")

# ###############################################################
# test code section
if __name__ == "__main__":
    print("="*50)
    print("programme de tetection de langue".upper())
    print("="*50)

    print(fileManager())
    #LanguageDetect.frequency(fileManager())
