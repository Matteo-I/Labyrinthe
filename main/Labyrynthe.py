from random import randrange as rd
from Cheetah.Template import Template
import webbrowser


class Cellule:
    def __init__(self, murNord, murEst, murSud, murOuest):
        self.murs={'N':murNord,'E':murEst, 'S':murSud,'O':murOuest}

    def __repr__(self):
        return str(self.murs)

    def generateclass(self):
        return " ".join([k for k,v in self.murs.items() if v])

class Labyrinthe:
    def __init__(self, hauteur, longueur):
        self.grille=self.construire_grille(hauteur, longueur)

    def __repr__(self):
        result=''
        for ligne in self.grille:
            for cell in ligne:
                result+=str(cell) 
            result+='\n'
        return result

    def construire_grille(self, hauteur, longueur):
        grille = []
        for i in range(hauteur):
            ligne = []
            for j in range(longueur):
                cellule = Cellule(True,True,True,True)
                ligne.append(cellule)
            grille.append(ligne)
        return grille

    def creer_passage(self, c1_lig, c1_col, c2_lig, c2_col):
        """ creer un passange entre deux cellules

        Args:
            c1_lig (int): x cell 1
            c1_col (int): y cell 1 
            c2_lig (int): x cell 2 
            c2_col (int): y cell 2
        """
        cellule1 = self.grille[c1_lig][c1_col]
        cellule2 = self.grille[c2_lig][c2_col]
        # cellule2 au Nord de cellule1
        if c1_lig - c2_lig == 1 and c1_col == c2_col:
            cellule1.murs['N'] = False
            cellule2.murs['S'] = False
          # cellule2 à l'Ouest de cellule1
        elif c1_col - c2_col == 1 and c1_lig == c2_lig:
            cellule1.murs['O'] = False
            cellule2.murs['E'] = False
            # cellule2 au Sud de cellule1
        elif c2_lig - c1_lig == 1 and c1_col == c2_col:
            cellule1.murs['S'] = False
            cellule2.murs['N'] = False
            # cellule2 à l'Est de cellule1
        elif c2_col - c1_col == 1 and c1_lig == c2_lig:
            cellule1.murs['E'] = False
            cellule2.murs['O'] = False

    def creer_labyrinthe(self, ligne, colonne, haut, long, nb_portes = 1):
        """ creer un labyrinthe

        Args:
            ligne (int): la ligne haute du labyrinthe
            colonne (int): la colone gauche du labyrinthe 
            haut (int): hauteur du labyrinthe
            long (int): longueur du labyrinthe
        """     
        if haut == 1 : # Cas de base
            for k in range(colonne,colonne+long-1):
                self.creer_passage(ligne, k, ligne, k+1)
        elif long == 1: # Cas de base
            for k in range(ligne,ligne+haut-1):
                self.creer_passage(k, colonne, k+1,colonne)
        else: # Appels récursifs
            if haut >= long:
                demi = haut//2
                self.creer_labyrinthe(ligne, colonne, demi,long)
                self.creer_labyrinthe(ligne + demi, colonne, haut-demi,long)
                for _ in range(nb_portes):
                    c = rd(colonne,colonne+long)
                    self.creer_passage(ligne+demi-1,c,ligne+demi,c)
            else:
                demi=long//2
                self.creer_labyrinthe(ligne,colonne,haut,demi)
                self.creer_labyrinthe(ligne,colonne+demi,haut,long-demi)
                for _ in range(nb_portes):    
                    l = rd(ligne,ligne+haut)
                    self.creer_passage(l,colonne+demi-1,l,colonne+demi)
    
    def generate_html(self):
        with open('/home/m.imbert/Bureau/NSI/Terminal/ProjetsTerm/Labyrythe/Labyrynthe/main/repr.html') as d:
            content="".join(d.readlines())
            
        t = Template(content,searchList=[{'grille':self.grille}])
        f = open('/home/m.imbert/Bureau/NSI/Terminal/ProjetsTerm/Labyrythe/Labyrynthe/main/labyrinthe.html', "w")
        f.write(str(t))
        f.close()




a=Labyrinthe(40,40)
a.creer_labyrinthe(0,0,40,40,4)
a.generate_html()
webbrowser.open('/home/m.imbert/Bureau/NSI/Terminal/ProjetsTerm/Labyrythe/Labyrynthe/main/labyrinthe.html')