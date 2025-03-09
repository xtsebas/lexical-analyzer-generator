# src/syntax_tree.py
from typing import Optional, Set
from src.model.nodo import Nodo
from src.utils.shunting_yard import shunting_yard
from model.tree import Tree

def convertir_a_posfijo(regex: str) -> str:
    """
    Convierte una expresión regular en notación infija a notación posfija utilizando el algoritmo Shunting Yard.
    
    Parámetros:
        regex (str): Expresión regular en notación infija.
    
    Retorna:
        str: Expresión regular en notación posfija.
    """
    postfix = shunting_yard(regex=regex)
    print('postfix -> '+postfix)
    return postfix

def construir_arbol(regex: str) -> Tree:
    """
    Construye el árbol sintáctico a partir de una expresión regualar.
    
    Parámetros:
        posfijo (str): Expresión regular en notación posfija.
    
    Retorna:
        Tree: árbol sintáctico construido.
    """
    postfijo = convertir_a_posfijo(regex)
    return Tree(expresion_postfija=postfijo)
     

def calcular_anulable(arbol: Tree) -> Tree:
    """
    Calcula la propiedad anulable para cada nodo del árbol sintáctico.
    
    Parámetros:
        Tree: árbol sintáctico.
    
    Retorna:
        Tree: árbol sintáctico con anulable construido.
    """
    print("\n====== Construcción de Anulable======\n")

    if arbol.raiz:
        arbol.calcular_anulable(arbol.raiz)
    
    return arbol 

def calcular_primera_pos(arbol: Tree) -> Tree:
    """
    Calcula la primera posición para cada nodo del árbol sintáctico.
    
    Parámetros:
        Tree: árbol sintáctico con anulable.
    
    Retorna:
        Tree: árbol sintáctico con funcion primera posicion construido.
    """

    print("\n====== Construcción de Funcion Primera Posicion======\n")

    if arbol.raiz:
        arbol.calcular_primeraPosicion(arbol.raiz)

    return arbol

def calcular_ultima_pos(arbol: Tree) -> Tree:
    """
    Calcula la última posición para cada nodo del árbol sintáctico.
    
    Parámetros:
        Tree: árbol sintáctico con anulable.
    
    Retorna:
        Tree: árbol sintáctico con funcion ultima posicion construido.
    """
    print("\n====== Construcción de Funcion Ultima Posicion======\n")

    if arbol.raiz:
        arbol.calcular_ultimaPosicion(arbol.raiz)

    return arbol

def calcular_siguiente_pos(arbol: Tree) -> Tree:
    """
    Calcula la siguiente posición para cada nodo del árbol sintáctico basado en la función siguiente.

    Parámetros:
        Tree: árbol sintáctico con anulable.
    
    Retorna:
        Tree: árbol sintáctico con funcion siguiente posicion construido.
    """
    print("\n====== Construcción de Funcion Siguiente Posicion======\n")

    if arbol.raiz:
        arbol.calcular_siguientePosicion(arbol.raiz)

    return arbol
