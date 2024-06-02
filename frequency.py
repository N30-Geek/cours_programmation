fr_ltrs_frq = { # fréqunce des lettre s dans la langue française
"A": 8.15,"B": 0.97,"C": 3.15,"D": 3.73,
"E": 17.39,"F": 1.12,"G": 0.97,"H": 0.85,
"I": 7.31,"J": 0.45,"K": 0.02,"L": 5.69,
"M": 2.87, "N": 7.12, "O": 5.28,"P": 2.80,
"Q": 1.21, "R": 6.64, "S": 8.14, "T": 7.22,
"U": 6.38, "V": 1.64, "W": 0.03, "X": 0.41,
"Y": 0.28, "Z": 0.15,
}


#r corpus letter frequency wikipedia
fr_coprus_wk = {
    "E": 12.10,
    "A": 7.11,
    "I": 6.59,
    "S": 6.51,
    "N": 6.39,
    "R": 6.07,
    "T": 5.92,
    "O": 5.02,
    "L": 4.96,
    "U": 4.49
}
## les grammes dans la langue française
fr_bgrms = ["ES","LE","EN","RE","DE","NT","TE","AI","ET","ER"] # bigramme les plus fréquent en français
fr_trgms = ["ENT","LES","AIT","QUE","EDE","DES","LLE","RES","ANT","TRE"] # trigramme les plus fréquent en français
fr_ttrgrms = ["MENT","ELLE","QUEL","EMEN","TION","DANS","IENT","ESDE","DELA","OMM"] # tetragramme les plus fréquent en français
fr_hxgrms = ["DANS","LEMENT","QUELLE","QUELQU","UELQUE","ENDANT","TAIENT","ENCORE","EMMENTD"] # hexagramme les plus fréquent en français



# if __name__ == "__main__":
#     for k, v in fr_ltrs_frq.items():
#         print(f"{k} = {v}")
    
#     print(f"{ "ENT" in ''.join(fr_trgms)}")
#     print(f"{"".join(fr_trgms)}")