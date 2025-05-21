class BoostInvalideException(Exception):
    pass

class Boost:
    def __init__(self, type_boost: int):
        self.type_boost = type_boost

    def get_type(self):
        return self.type_boost

    def get_boost_energie(self):
        if self.type_boost == 1:
            return 60
        elif self.type_boost == 2:
            return 80
        elif self.type_boost == 3:
            return 120
        else:
            raise BoostInvalideException("type de boost invalide")

class Animal:
    def __init__(self, energie_initiale: int):
        self.energie = energie_initiale

    def nourrir(self, boost: Boost):
        self.energie += boost.get_boost_energie()

    def attaquer(self, autre_animal: 'Animal'):
        autre_animal.energie -= 50

    def get_energie(self):
        return self.energie

