from behave import given, when, then
from main import Animal, Boost

# Contexte de stockage des animaux
@given('un animal nommé {nom} avec une énergie initiale de {energie:d}')
def step_creer_animal(context, nom, energie):
    animal = Animal(nom, f"{nom.lower()}@savane.fr", energie)
    if not hasattr(context, 'animaux'):
        context.animaux = {}
    context.animaux[nom] = animal
    context.animal_courant = animal

@when('il utilise un boost de type {type_boost:d}')
def step_utiliser_boost(context, type_boost):
    boost = Boost(type_boost)
    context.animal_courant.nourrir(boost)

@then("l'énergie finale de l'animal est {energie_attendue:d}")
def step_verifier_energie(context, energie_attendue):
    energie_actuelle = context.animal_courant.get_energie()
    assert energie_actuelle == energie_attendue, f"Énergie attendue {energie_attendue}, obtenue {energie_actuelle}"

@when('il publie le message {message}')
def step_publier_message(context, message):
    context.animal_courant.publier(message)

@then('la dernière publication affichée est {publication}')
def step_verifier_derniere_publication(context, publication):
    derniere_pub = context.animal_courant.fil_actualite[0].afficher()
    assert derniere_pub == publication, f"Publication attendue: {publication}, obtenue: {derniere_pub}"
