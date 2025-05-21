@tag Feature: Gestion énergie Animal avec Boost et Attaque

  En tant que Développeur 
  Je veux gérer l'énergie des objets Animal en interaction avec des Boosts 
  Et permettre aux animaux d’interagir entre eux via des attaques
  Afin de modéliser dynamiquement les changements d'énergie dans un système de simulation

Scenario Outline: odification de l'énergie par Boost 
Given un animal avec une énergie initiale de <energie_initiale> 
And un boost de type <type_boost> 
When l'animal reçoit le boost 
Then l'énergie finale de l'animal doit être égale à <energie_finale>

Examples:
  | energie_initiale | type_boost | energie_finale |
  | 100              | 1          | 160            |
  | 100              | 2          | 180            |
  | 100              | 3          | 220            |
  | 150              | 2          | 230            |

 Scenario Outline: Attaque entre deux animaux
    Given un animal A avec une énergie initiale de <energie_A_initiale>
    And un animal B avec une énergie initiale de <energie_B_initiale>
    When l'animal A attaque l'animal B
    Then l'énergie finale de l'animal B doit être <energie_B_finale>

    Examples:
      | energie_A_initiale | energie_B_initiale | energie_B_finale |
      | 100                | 100                |  50              |
      | 150                | 70                 |  20              |
      | 200                | 120                |  70              |

  

  
