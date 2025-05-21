from behave import given, when, then
from main import Animal, Boost

@given('un animal avec une énergie initiale de {energie_initiale:d}')
def creer_animal(context, energie_initiale):
    context.animal = Animal(energie_initiale)

@given('un boost de type {type_boost:d}')
def creer_boost(context, type_boost):
    context.boost = Boost(type_boost)

@when("l'animal reçoit le boost")
def animal_recoit_boost(context):
    context.animal.nourrir(context.boost)

@then("l'énergie finale de l'animal doit être égale à {energie_finale:d}")
def verifier_energie_finale(context, energie_finale):
    assert context.animal.get_energie() == energie_finale

# Scenario Attaque
@given("un animal A avec une énergie initiale de {energie_A_initiale:d}")
def animal_a(context, energie_A_initiale):
    context.animal_A = Animal(energie_A_initiale)

@given("un animal B avec une énergie initiale de {energie_B_initiale:d}")
def animal_b(context, energie_B_initiale):
    context.animal_B = Animal(energie_B_initiale)

@when("l'animal A attaque l'animal B")
def attaque_animaux(context):
    context.animal_A.attaquer(context.animal_B)

@then("l'énergie finale de l'animal A doit être {energie_A_finale:d}")
def verifier_energie_A(context, energie_A_finale):
    assert context.animal_A.get_energie() == energie_A_finale

@then("l'énergie finale de l'animal B doit être {energie_B_finale:d}")
def verifier_energie_B(context, energie_B_finale):
    assert context.animal_B.get_energie() == energie_B_finale
