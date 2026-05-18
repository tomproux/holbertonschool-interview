#!/usr/bin/python3
"""Module pour travailler avec le triangle de Pascal."""


def pascal_triangle(n):
    """Retourne le triangle de Pascal sous forme de liste de listes.

    Args:
        n (int): Nombre de lignes du triangle à générer.

    Returns:
        list: Triangle de Pascal de taille n.
              Retourne une liste vide si n <= 0 ou si n n'est pas un entier.
    """
    if not isinstance(n, int) or n <= 0:
        return []

    triangle = []
    for ligne in range(n):
        if ligne == 0:
            triangle.append([1])
            continue

        precedent = triangle[-1]
        rang = [1]
        for i in range(len(precedent) - 1):
            rang.append(precedent[i] + precedent[i + 1])
        rang.append(1)
        triangle.append(rang)

    return triangle
