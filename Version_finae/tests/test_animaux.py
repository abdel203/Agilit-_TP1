import unittest
from main import Animal, Boost, Publication, Commentaire

class TestAnimauxSocial(unittest.TestCase):

    def test_utilisation_boost(self):
        lion = Animal("Lion", "lion@savane.fr", 100)
        boost = Boost(2)  # +80
        lion.nourrir(boost)
        self.assertEqual(lion.get_energie(), 180)
        self.assertEqual(lion.fil_actualite[0].afficher(), "Lion a publié : a utilisé un boost type 2 (+80)")

    def test_attaque(self):
        tigre = Animal("Tigre", "tigre@jungle.fr", 150)
        lion = Animal("Lion", "lion@savane.fr", 100)
        tigre.attaquer(lion)
        self.assertEqual(lion.get_energie(), 50)
        self.assertEqual(tigre.fil_actualite[0].afficher(), "Tigre a publié : a attaqué Lion (-50 énergie)")

    def test_publication_manuelle(self):
        ours = Animal("Ours", "ours@forêt.fr", 90)
        pub = ours.publier("Bonjour à tous")
        self.assertEqual(pub.afficher(), "Ours a publié : Bonjour à tous")
        self.assertEqual(ours.fil_actualite[0], pub)

    def test_commentaire(self):
        lion = Animal("Lion", "lion@savane.fr", 100)
        tigre = Animal("Tigre", "tigre@jungle.fr", 120)
        pub = lion.publier("Je suis le roi")
        com = Commentaire("Bravo !", tigre, pub)
        self.assertEqual(com.afficher(), "Tigre a commenté : Bravo !")

    def test_boost_invalide(self):
        with self.assertRaises(ValueError) as ctx:
            Boost(99).get_boost_energie()
        self.assertIn("Type de boost invalide", str(ctx.exception))

if __name__ == '__main__':
    unittest.main()