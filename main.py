#### Imports et définition des variables globales
"""
Module contenant deux fonctions d'encodage RLE (itérative et récursive).
"""
# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument 
        selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    char=[s[0]]
    count=[1]
    k=1
    n=len(s)
    while k<n:
        if s[k]==s[k-1]:
            count[-1]+=1
        else:
            char.append(s[k])
            count.append(1)
        k+=1
    return list(zip(char,count))


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument 
        selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # votre code ici
    n=len(s)
    # cas de base
    if n==0:
        return []
    if n==1:
        return [(s[0],1)]
    # recherche nombre de caractères identiques au premier
    k=0
    while k<n and s[k]==s[0]:
        k+=1
    block = (s[0],k)
    # appel récursif
    reste = artcode_r(s[k:])
    return [block]+reste
#### Fonction principale


def main():
    """Fonction principale exécutant quelques tests simples."""
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
