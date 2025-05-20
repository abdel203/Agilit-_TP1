# Rapport - Classe Animal

## Introduction

Ce rapport détaille le processus complet de création, d'instanciation et de test d'une application Java simple à l'aide de l'environnement de développement BlueJ. Il présente également l'interaction entre deux classes (`Animal` et `Boost`).


## Étapes de Développement

### Création du Projet

Le projet nommé **« FirstProject »** a été initialement créé via BlueJ, un environnement graphique qui permet une gestion visuelle simple des projets Java.

### Création de la Classe « Animal »

Une classe intitulée `Animal` a été définie en premier lieu. Cette classe représente notre classe « fétiche », identifiée de manière unique dans le cadre du projet.

Après sa création, elle a été compilée avec succès pour s'assurer de l'absence d'erreurs syntaxiques. Un premier objet nommé `animal1` a ensuite été instancié, permettant une visualisation directe dans BlueJ.

!![ee](Projet_metha_images/Instancier_Classe.png)
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

## Table des matières

- [Introduction](#introduction)
- [Étapes de Développement](#étapes-de-développement)
  - [Création du Projet](#création-du-projet)
  - [Création de la Classe « Animal »](#création-de-la-classe-animal)
  - [Définition des Attributs et Méthodes](#définition-des-attributs-et-méthodes)
  - [Exécution Interactive](#exécution-interactive)
  - [Tests Unitaires et Validation](#tests-unitaires-et-validation)
  - [Ajout d'une Classe Associée « Boost »](#ajout-dune-classe-associée-boost)
  - [Utilisation des Fixtures dans les Tests Unitaires](#utilisation-des-fixtures-dans-les-tests-unitaires)
