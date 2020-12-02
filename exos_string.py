'''
1/ Coder une fonction qui, à partir d’un mot, renvoie le même mot mais avec ses lettres inversées. 
Par exemple, “algo” renverra “ogla”, et “théière” renverra “erèiéht”. 
Conseil   :   vous   pouvez   parcourir   une   chaîne   en   commençant   par   la   fin.
'''

mot_un = "algo"
mot_deux = "théière"
phrase = "qui vole un oeuf vole un boeuf"
def inversemot (mot) :
    retientlettre = ""
    for i in range (1, len(mot)+1) :
        print(retientlettre)
    return retientlettre
    
inversemot(mot_deux)  

'''
2/ Coder une fonction qui, à partir d’un mot, renvoie son nombre de consonnes. 
Conseil   :   comptez   le   nombre   de   voyelles,   et   déduisez-en   le   nombre   de   consonnes.   
Pour   compter   le   nombre   de voyelles,   il   faudra   parcourir   la   chaîne,   et,   pour   chaque   lettre,   
regarder   s’il   s’agit   d’une   voyelle   ;   si   oui,   vous pourrez   alors   incrémenter   un   compteur.   
Vous   obtenez   ensuite   la   solution   en   comparant   le   résultat   avec   le nombre   total   de   lettres   dans   le   mot. 
'''

def renvoiconsonne(mot) :
    compteurvoyelle = 0
    for i in range (0, len(mot)) :
        if (mot[i]=="a" or mot[i]=="o" or mot[i]=="i" or mot[i]=="e" or mot[i]=="u" or mot[i]=="y"):
            compteurvoyelle += 1
    nombreconsonne = len(mot) - compteurvoyelle    
    return nombreconsonne
    
'''renvoiconsonne(mot_un)'''

'''3/ Coder un programme qui permet à l’utilisateur de crypter et décrypter des messages secrets grâce au chiffrement de César. 
Le voilà décrit sur Wikipédia en Décembre 2020 : '''

def chiffrementcesar(mot, clef) :
    mot = mot.lower()
    i = 0
    motchiffre = ""
    clef26 = 26 - clef
    for i in range (0, len(mot)) :
        if (ord(mot[i])== ord(" ")) :
            motchiffre += chr(32)
        else :
            chiffrement = ord(mot[i])
            if (chiffrement >= ord("a") and chiffrement <= ord(chr(96+clef26))) :
                motchiffre += chr(chiffrement + clef)
            else :
                motchiffre += chr(chiffrement + clef - 26)
    print(motchiffre)
    return motchiffre
    
chiffrementcesar(input("Veuillez saisir une phrase à crypter \n"), 3)

input ()
