from typing import Dict, Any
from regex_afd.src.model.afd import AFD
from regex_afd.src.parser import parsear_regex, aumentar_regex 
from regex_afd.src.syntax_tree import construir_arbol, calcular_anulable, calcular_primera_pos, calcular_ultima_pos, calcular_siguiente_pos
from regex_afd.src.build_afd import construir_afd
from regex_afd.src.simulation import evaluar_cadena
from regex_afd.src.minimization import minAFD

#Parsea expresiones regulares y las convierte en un AFD
# Input: expresiones regulares del archivo .yal
# Output: estructura de datos representando un AFD
def parse_regex(cadena, regex):
    afd = regex_to_automaton(regex=regex)
    afd =  minAFD(afd)
    aceptada = evaluar_cadena(afd, cadena)
    if aceptada:
        print(f"La cadena '{cadena}' es aceptada por el AFD.")
    else:
        print(f"La cadena '{cadena}' NO es aceptada por el AFD.")


# Convierte una expresión regular en un autómata finito
# Input: expresión regular
# Output: estructura del autómata
def regex_to_automaton(regex):
    """
    Aplica el método directo (Followpos Algorithm) para convertir una expresión regular a un AFD.

    Parámetros:
        regex (str): Expresión regular de entrada.

    Retorna:
        AFD: El AFD resultante representado como un diccionario que incluye:
            - "Q": Conjunto de estados.
            - "A": Alfabeto.
            - "T": Función de transición.
            - "q0": Estado inicial.
            - "F": Conjunto de estados de aceptación.
    """
    
    # 1 agregar concatenación y quitar los operadores que no reconoce el método directo 
    regex_parse = parsear_regex(regex=regex)
    
    # 2 aumentar la expresion con #
    regex_aumentada = aumentar_regex(regex=regex_parse)
    
    # 3 arbol sintactico
    arbol = construir_arbol(regex=regex_aumentada)
    
    # 4 Calcular anulable

    arbol = calcular_anulable(arbol)

    # 5 Calcular Funcion Primera Posicion
    arbol = calcular_primera_pos(arbol)

    # 6 Calcular Funcion Ultima Posicion
    arbol = calcular_ultima_pos(arbol)

    # 7 Calcular Funcion Siguiente Posicion
    arbol = calcular_siguiente_pos(arbol)
    
    print("\nFollowpos (Posición : Caracter : {posiciones siguientes}):")
    for pos, info in sorted(arbol.followpos.items()):
        print(f"{pos} : '{info['valor']}' : {info['siguientes']}")

    #8, 9 tabla de transiciones y AFD
    afd = construir_afd(arbol=arbol)
    afd.imprimir()
    
    return afd