class Scorer(object):

    score = 0
    score_frame = 0
    frame = 1
    lancer = 0
    facteur_spare = 1
    facteur_strike = 1

    def afficher_score(self):
        return self.score

    def effectuer_un_lancer(self, nb_quilles_tombees=0):
        self.score += self.facteur_spare*self.facteur_strike*nb_quilles_tombees
        self.score_frame += nb_quilles_tombees
        self.lancer += 1
        self._gerer_spare()
        self._gerer_strike()

    def _gerer_spare(self):
        self.facteur_spare = 1
        if self.lancer > 1: # Deuxième lancer
            if self.score_frame == 10: # Spare
                self.facteur_spare = 2
            self.passer_au_frame_suivant()

    def _gerer_strike(self):
        if self.lancer == 1: # Premier lancer
            if self.score_frame == 10: # Strike
                self.facteur_strike = 2
                self.passer_au_frame_suivant()
        else: # Deuxième lancer
            if self.facteur_strike == 2: # Strike au frame précédent
                self.facteur_strike = 1
            self.passer_au_frame_suivant()

    def passer_au_frame_suivant(self):
        self.frame += 1
        self.lancer = 0
        self.score_frame = 0
