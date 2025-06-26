Feature: Simulation sociale des Animaux

  En tant que Développeur
  Je veux permettre aux animaux d’agir et de publier sur un réseau social
  Afin de suivre leurs actions et leurs messages dans un fil d’actualité

  Scenario Outline: Utilisation d’un boost par un animal
    Given un animal nommé <nom> avec une énergie initiale de <energie_initiale>
    When il utilise un boost de type <type_boost>
    Then l'énergie finale de l'animal est <energie_finale>

    Examples:
      | nom   | energie_initiale | type_boost | energie_finale |
      | Lion  | 100              | 1          | 160            |
      | Tigre | 120              | 2          | 200            |

  Scenario Outline: Publication manuelle par un animal
  Given un animal nommé <nom> avec une énergie initiale de <energie>
  When il publie le message <message>
  Then la dernière publication affichée est <publication>

  Examples:
    | nom   | energie | message             | publication                        |
    | Ours  | 90      | Bonjour à tous      | Ours a publié : Bonjour à tous     |
    | Lion  | 100     | Je suis le roi      | Lion a publié : Je suis le roi     |

