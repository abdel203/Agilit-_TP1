from typing import List

# ─── Boost ────────────────────────────────────────────────────────────────

class Boost:
    def __init__(self, type_boost: int):
        self.type_boost = type_boost

    def get_type(self) -> int:
        return self.type_boost

    def get_boost_energie(self) -> int:
        if self.type_boost == 1:
            return 60
        elif self.type_boost == 2:
            return 80
        elif self.type_boost == 3:
            return 120
        else:
            raise ValueError("Type de boost invalide")

# ─── Publication & Commentaire ────────────────────────────────────────────

class Publication:
    def __init__(self, texte: str, auteur: 'Utilisateur'):
        self.texte = texte
        self.auteur = auteur

    def afficher(self) -> str:
        return f"{self.auteur.nom} a publié : {self.texte}"

class Commentaire:
    def __init__(self, texte: str, auteur: 'Utilisateur', publication: Publication):
        self.texte = texte
        self.auteur = auteur
        self.publication = publication

    def afficher(self) -> str:
        return f"{self.auteur.nom} a commenté : {self.texte}"

# ─── Utilisateur & Animal ────────────────────────────────────────────────

class Utilisateur:
    def __init__(self, nom: str, email: str):
        self.nom = nom
        self.email = email
        self.fil_actualite: List[Publication] = []

    def publier(self, texte: str) -> Publication:
        if not texte:
            raise ValueError("Le message ne peut pas être vide.")
        if len(texte) > 280:
            raise ValueError("Le message dépasse la limite autorisée.")
        pub = Publication(texte, self)
        self.fil_actualite.insert(0, pub)
        return pub

class Animal(Utilisateur):
    def __init__(self, nom: str, email: str, energie_initiale: int):
        super().__init__(nom, email)
        self.energie = energie_initiale

    def nourrir(self, boost: Boost):
        points = boost.get_boost_energie()
        self.energie += points
        self.publier(f"a utilisé un boost type {boost.get_type()} (+{points})")

    def attaquer(self, cible: 'Animal'):
        cible.energie -= 50
        self.publier(f"a attaqué {cible.nom} (-50 énergie)")

    def get_energie(self) -> int:
        return self.energie

# ─── Réseau Social ───────────────────────────────────────────────────────

class ReseauSocial:
    def __init__(self):
        self.utilisateurs: List[Utilisateur] = []

    def ajouter_utilisateur(self, u: Utilisateur):
        self.utilisateurs.append(u)

    def get_utilisateurs(self) -> List[Utilisateur]:
        return self.utilisateurs

    def afficher_fil(self, u: Utilisateur):
        print(f"\n— Fil de {u.nom} —")
        for pub in u.fil_actualite:
            print("  ", pub.afficher())

# ─── Démonstration ───────────────────────────────────────────────────────

if __name__ == "__main__":
    # 1) Création du réseau
    reseau = ReseauSocial()

    # 2) Création de deux animaux
    lion = Animal("Lion", "lion@savane.fr", energie_initiale=100)
    tigre = Animal("Tigre", "tigre@jungle.fr", energie_initiale=120)
    reseau.ajouter_utilisateur(lion)
    reseau.ajouter_utilisateur(tigre)

    # 3) Boosts et attaque
    lion.nourrir(Boost(2))  # +80
    lion.attaquer(tigre)    # -50 pour tigre
    tigre.nourrir(Boost(1)) # +60

    # 4) Commentaire
    pub = lion.fil_actualite[0]
    comm = Commentaire("Bien joué, Lion !", tigre, pub)

    # 5) Énergies finales
    print(f"\nÉnergie finale de {lion.nom} : {lion.get_energie()}")
    print(f"Énergie finale de {tigre.nom} : {tigre.get_energie()}")

    # 6) Affichage des fils d’actualité
    reseau.afficher_fil(lion)
    reseau.afficher_fil(tigre)

    # 7) Affichage du commentaire
    print("\nCommentaire seul :")
    print(" ", comm.afficher())
