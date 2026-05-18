#!/usr/bin/python3
"""Module pour vérifier si tous les coffres peuvent être ouverts.

Chaque coffre est représenté par une liste de clés. Une clé ouvre
le coffre dont l'index est égal à la valeur de la clé. Le premier
coffre `boxes[0]` est déverrouillé au départ.
"""


def canUnlockAll(boxes):
    """Détermine si tous les coffres peuvent être ouverts.

    Args:
        boxes (list of list): Chaque sous-liste représente les clés contenues
                              dans un coffre.

    Returns:
        bool: True si tous les coffres peuvent être ouverts, sinon False.
    """
    # Si la liste est vide, il n'y a pas de coffre accessible.
    if not boxes:
        return False

    # Coffres déjà ouverts et clés disponibles.
    opened = {0}
    keys = set(boxes[0])
    changed = True

    # Tant qu'on ouvre de nouveaux coffres, on continue d'explorer.
    while changed:
        changed = False
        for idx, box in enumerate(boxes):
            # Ouvre une box si on a la clé et qu'il n'est pas déjà ouvert.
            if idx not in opened and idx in keys:
                opened.add(idx)
                keys.update(box)
                changed = True

    # Tous les coffres sont ouverts si le nombre de coffres ouverts
    # correspond au nombre total de coffres.
    return len(opened) == len(boxes)
