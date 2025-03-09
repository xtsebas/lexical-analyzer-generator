import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.stack import Stack

#referencia  a https://github.com/xtsebas/regex_to_AFD/blob/main/Controller/postfix.py

def shunting_yard(regex: str) -> str:
    """Convierte una expresión regular en notación infija a notación postfija."""
    output = []
    pila_operadores = Stack()

    # Precedencia de operadores (mayor número = mayor precedencia)
    precedencia = {
        "*": 3,  # Cerradura de Kleene
        ".": 2,  # Concatenación
        "|": 1   # Unión (alternancia)
    }

    operadores = set(precedencia.keys())

    for token in regex:
        if token not in operadores and token not in "()":  # Si es un operando (letra o 'E')
            output.append(token)

        elif token in operadores:  # Si es un operador
            while (not pila_operadores.is_empty() and 
                   pila_operadores.peek() in operadores and 
                   precedencia[pila_operadores.peek()] >= precedencia[token]):  
                output.append(pila_operadores.pop())
            pila_operadores.push(token)

        elif token == '(':  # Si es un paréntesis izquierdo
            pila_operadores.push(token)

        elif token == ')':  # Si es un paréntesis derecho
            while not pila_operadores.is_empty() and pila_operadores.peek() != '(':
                output.append(pila_operadores.pop())
            pila_operadores.pop()  # Eliminar el paréntesis izquierdo

    # Vaciar la pila de operadores al final
    while not pila_operadores.is_empty():
        output.append(pila_operadores.pop())

    return ''.join(output)