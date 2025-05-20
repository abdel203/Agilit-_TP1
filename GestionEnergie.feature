@tag Feature: Gestion énergie Animal avec Boost

En tant que Développeur 
Je veux gérer l'énergie des objets Animal en interaction avec des Boosts 
Afin de permettre une gestion dynamique de leur énergie

Scenario Outline: Modification de l'énergie par Boost 
Given un animal avec une énergie initiale de <energie_initiale> 
And un boost de type <type_boost> avec énergie <energie_boost> 
When l'animal reçoit le boost 
Then l'énergie finale de l'animal doit être égale à <energie_finale>

Examples:
  | energie_initiale | type_boost | energie_boost | energie_finale |
  | 100              | 1          | 60            | 160            |
  | 100              | 2          | 80            | 180            |
  | 100              | 3          | 120           | 220            |
  | 150              | 2          | 80            | 230            |

  Scenario Outline: Refus d'un boost avec type invalide 
  Given un animal avec une énergie initiale de <energie_initiale> 
  And un boost avec un type <type_boost> invalide
  When l'animal reçoit le boost 
  Then le système refuse avec le message d’erreur

  Examples:
  | energie_initiale | type_boost | messageErreur            |
  | 100              | -1         | "type de boost invalide" |
  | 100              | 4          | "type de boost invalide" |

  

  
