#!/usr/bin/python3
"""Module pour travailler avec le triangle de Pascal."""


def pascal_triangle(n):
    """Retourne le triangle de Pascal selon l'entrée.

    Cette fonction prend un paramètre `n` et vérifie s'il s'agit
    exactement du type `int`. Si `n` est un entier et que sa valeur
    est inférieure ou égale à 0, la fonction renvoie une liste vide.
    Sinon, elle renvoie simplement `n`.

    Args:
        n: Valeur d'entrée fournie pour générer le triangle.

    Returns:
        list: Une liste vide si `n` est un entier négatif ou nul.
        n: La valeur originale de `n` si `n` est un entier strictement positif.
    """
    # Vérifie explicitement le type de `n`.
    if n is int:
        # Si `n` est un entier inférieur ou égal à zéro, on renvoie une liste vide.
        if n <= 0:
            return []
        else:
            # Si `n` est un entier strictement positif, on renvoie la valeur telle quelle.
            return n
