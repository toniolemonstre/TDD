class Scorer(object):

    score = 0
    score_frame = 0
    frame = 1
    lancer = 1
    facteur_spare = 1
    facteur_strike = 1

    def afficher_score(self):
        return self.score

    def effectuer_un_lancer(self, nb_quilles_tombees=0):
        self.score += self.facteur_spare*self.facteur_strike*nb_quilles_tombees
        self.facteur_spare = 1
        self.score_frame += nb_quilles_tombees
        self.lancer += 1
        if self.lancer > 2:
            if self.score_frame == 10:
                self.facteur_spare = 2
            if self.facteur_strike == 2:
                self.facteur_strike = 1
            self.passer_au_frame_suivant()
        else:
            if self.score_frame == 10:
                self.facteur_strike = 2
                self.passer_au_frame_suivant()

    def passer_au_frame_suivant(self):
        self.frame += 1
        self.lancer = 1
        self.score_frame = 0
