import unittest
from bowling import Scorer

class TestScore(unittest.TestCase):

    def test_au_debut_le_score_est_zero(self):
        scorer = Scorer()
        self.assertEqual(scorer.afficher_score(), 0)

    def test_apres_deux_lancers_nuls_le_score_est_zero(self):
        scorer = Scorer()
        scorer.effectuer_un_lancer()
        scorer.effectuer_un_lancer()
        self.assertEqual(scorer.afficher_score(), 0)

    def test_apres_un_lancer_nul_et_un_lancer_une_quille(self):
        scorer = Scorer()
        scorer.effectuer_un_lancer()
        scorer.effectuer_un_lancer(1)
        self.assertEqual(scorer.afficher_score(), 1)

    def test_apres_un_lancer_une_quille_et_un_lancer_nul(self):
        scorer = Scorer()
        scorer.effectuer_un_lancer(1)
        scorer.effectuer_un_lancer()
        self.assertEqual(scorer.afficher_score(), 1)

    def test_apres_un_lancer_deux_et_un_lancer_trois_quilles_le_score_est_cinq(self):
        scorer = Scorer()
        scorer.effectuer_un_lancer(2)
        scorer.effectuer_un_lancer(3)
        self.assertEqual(scorer.afficher_score(), 5)

    def test_apres_un_lancer_trois_quilles_un_lancer_sept_quilles_et_un_lancer_cinq_quilles(self):
        scorer = Scorer()
        scorer.effectuer_un_lancer(3)
        scorer.effectuer_un_lancer(7)
        scorer.effectuer_un_lancer(5)
        self.assertEqual(scorer.afficher_score(), 20)

    def test_apres_un_lancer_trois_quilles_un_lancer_sept_quilles_un_lancer_cinq_quilles_un_lancer_une_quille(self):
        scorer = Scorer()
        scorer.effectuer_un_lancer(3)
        scorer.effectuer_un_lancer(7)
        scorer.effectuer_un_lancer(5)
        scorer.effectuer_un_lancer(1)
        self.assertEqual(scorer.afficher_score(), 21)

    def test_apres_un_lancer_dix_quilles_un_lancer_cinq_quilles_un_lancer_une_quille(self):
        scorer = Scorer()
        scorer.effectuer_un_lancer(10)
        scorer.effectuer_un_lancer(5)
        scorer.effectuer_un_lancer(1)
        self.assertEqual(scorer.afficher_score(), 22)

    def test_apres_un_lancer_dix_quilles_un_lancer_cinq_quilles_un_lancer_une_quille_un_lancer_deux_quilles(self):
        scorer = Scorer()
        scorer.effectuer_un_lancer(10)
        scorer.effectuer_un_lancer(5)
        scorer.effectuer_un_lancer(1)
        scorer.effectuer_un_lancer(2)
        self.assertEqual(scorer.afficher_score(), 24)