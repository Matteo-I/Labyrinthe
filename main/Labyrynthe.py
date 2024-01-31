from random import randint as rd

class Cellule:
    def __init__(self, murNord, murEst, murSud, murOuest):
        self.murs={'N':murNord,'E':murEst, 'S':murSud,'O':murOuest}
    

    def __repr__(self):
      return str(self.murs)


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



    def creer_labyrinthe(self, ligne, colonne, haut, long):
      if haut == 1 : # Cas de base
        for k in range(colonne,colonne+long-1):
            self.creer_passage(ligne, k, ligne, k+1)
      elif long == 1: # Cas de base
        for k in range(ligne,ligne+haut-1):
            self.creer_passage(k, colonne, k+1,colonne)
      else: # Appels récursifs
        pass

a=Labyrinthe(4,4)
a.creer_labyrinthe(1,1,3,1)

b=Labyrinthe(4,4)
b.creer_labyrinthe(2,1,1,3)

print(a)
print(b)
