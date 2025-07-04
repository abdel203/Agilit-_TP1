# Rapport - Classe Animal

## Introduction

Ce rapport détaille le processus complet de création, d'instanciation et de test d'une application Java simple à l'aide de l'environnement de développement BlueJ. Il présente également l'interaction entre deux classes (`Animal` et `Boost`).


## Étapes de Développement

### Création du Projet

Le projet nommé **« FirstProject »** a été initialement créé via BlueJ, un environnement graphique qui permet une gestion visuelle simple des projets Java.

### Création de la Classe « Animal »

Une classe intitulée `Animal` a été définie en premier lieu. Cette classe représente notre classe « fétiche », identifiée de manière unique dans le cadre du projet.

Après sa création, elle a été compilée avec succès pour s'assurer de l'absence d'erreurs syntaxiques. Un premier objet nommé `animal1` a ensuite été instancié, permettant une visualisation directe dans BlueJ.

!![](Agilit-_TP1/Projet_metha_images/Instancier_Classe.png)
!![](Projet_metha_images/Création_et_compilation_classe.png)

### Définition des Attributs et Méthodes

La classe `Animal` a été enrichie par trois attributs principaux :

- `nom` (String)
- `age` (int)
- `energie` (int, initialement 100)

!![](Projet_metha_images/variable_animal.png)

Des méthodes spécifiques ont été ajoutées pour interagir avec ces attributs :

- `afficherEnergie()` : affiche l'énergie actuelle.
- `nourrir(Boost boost)` : augmente l'énergie selon un objet `Boost`.
- `attaquer(Animal an)` : diminue l'énergie d'un autre animal.
- `getEnergie()` : accesseur retournant l'énergie courante.

!![](Projet_metha_images/animal_methode.png)

### Exécution Interactive

Une instanciation interactive de la méthode `nourrir` a permis d'observer directement son effet sur l'état interne de l'objet. Après exécution, l'énergie initiale (100) de l'animal est passée à 150, confirmant le bon fonctionnement de la méthode.

!![](Projet_metha_images/nourrir_effet.png)

### Tests Unitaires et Validation

Des tests unitaires (`testAttaquer()` et `testNourrir()`) ont été créés à l'aide de l'environnement de test de BlueJ. Leur exécution réussie, indiquée par une barre verte, a validé le comportement attendu des méthodes.

!![](Projet_metha_images/Tester_methode_classe.png)

### Ajout d'une Classe Associée « Boost »

Une seconde classe `Boost` a été créée et associée de façon unidirectionnelle à la classe `Animal` (multiplicité 0..1 à 0..1). Elle contient un attribut unique :

- `type` (int)

Et une méthode principale :

- `Boost_energie()` : retourne la quantité d'énergie ajoutée selon le type du boost (60, 80 ou 120).

La classe `Animal` collabore avec `Boost` via la méthode `nourrir(Boost boost)`, qui utilise directement la valeur retournée par `Boost_energie()`.

!![](Projet_metha_images/boost_variable.png)
!![](Projet_metha_images/boost_methodes.png)

### Utilisation des Fixtures dans les Tests Unitaires

Pour garantir la reproductibilité des tests, une fixture `setUp()` a été définie, instanciant systématiquement les objets suivants avant chaque test :

- Deux objets `Animal` : `animal1` et `animal2`
- Un objet `Boost` : `boost1`

Tous les tests utilisant cette fixture ont abouti à un succès, confirmé par une barre verte.

!![](Projet_metha_images/Test_fixture(13).png)
!![](Projet_metha_images/Question_12.png)




# 🐾Projet Animal Boost – BDD avec Behave

Ce projet simule des animaux capables de recevoir de l’énergie via des boosts, ou de se battre.  
On y applique le **BDD (Behavior Driven Development)** avec [Behave](https://behave.readthedocs.io/).

pour :

- Gérer l'énergie d’un animal.
- Appliquer un boost selon son type (1, 2, 3).
- Permettre à un animal d’en attaquer un autre.
- Tester tout ça.

---

## Histoire du projet

Dans un univers d’animaux, chaque créature vit en équilibre avec son énergie.  
Certaines reçoivent des boosts pour devenir plus puissantes. D’autres choisissent de se battre pour survivre.  

Le défi : simuler ce monde avec du code, tout en s’assurant que chaque règle de comportement (gain d’énergie, combat, perte) fonctionne parfaitement.  

##  Arborescence

```bash
ProjetAnimalBoost/
├── main.py                      # Classes métier
└── features/
    ├── gestion_energie.feature  # Scénarios BDD
    └── steps/
        └── steps_gestion_energie.py  # Étapes Python
```

##  Test avec Behave

Les scénarios de test ont été définis en Gherkin dans le fichier `gestion_energie.feature`. Chaque scénario décrit un comportement attendu du système : augmentation de l’énergie après un boost, ou réduction de l’énergie après une attaque.

Les étapes correspondantes ont été implémentées dans `steps/steps_gestion_energie.py` à l’aide de la syntaxe `@given`, `@when`, `@then` de Behave, et sont directement reliées aux classes métier `Animal` et `Boost` définies dans `main.py`.

###  Exécution des tests

Les tests ont été lancés avec la commande suivante :

```bash
behave
```
Feature: Gestion énergie Animal avec Boost et Attaque
  Scenario Outline: Modification de l'énergie par Boost     ✅ Passed
  Scenario Outline: Attaque entre deux animaux              ✅ Passed

2 features passed, 0 failed
7 scenarios passed, 0 failed

### Resumé :

Chaque scénario a été exécuté avec succès, validant les comportements suivants :

    Le type de boost détermine l'énergie ajoutée à l’animal (60, 80, 120 selon le type 1, 2 ou 3).

    Une attaque diminue systématiquement l’énergie de l’animal ciblé de 50 points.

    Les énergies finales obtenues correspondent aux valeurs attendues dans les scénarios.
