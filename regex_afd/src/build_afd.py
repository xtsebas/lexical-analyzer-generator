from typing import Set, Dict, Tuple, Any
from model.afd import AFD
from model.tree import Tree

def construir_afd(arbol: Tree) -> AFD:
    """
    Construye el AFD usando la primera posición de la raíz del árbol como estado inicial.
    """
    followpos = arbol.followpos
    primera_pos_raiz = arbol.raiz.primera_pos
    pos_final = max(followpos.keys())  # Última posición es la del '#'

    estados_map = {}
    transiciones = {}
    estados_finales = set()
    alfabeto = set()

    estado_inicial = frozenset(primera_pos_raiz)
    estados_pendientes = [estado_inicial]
    estados_map[estado_inicial] = 'q_0'
    contador_estados = 1

    while estados_pendientes:
        estado_actual = estados_pendientes.pop()
        nombre_estado_actual = estados_map[estado_actual]
        transiciones[nombre_estado_actual] = {}

        simbolos = {}
        for posicion in estado_actual:
            valor = followpos[posicion]['valor']
            siguientes = followpos[posicion]['siguientes']
            if valor == '#':
                continue

            alfabeto.add(valor)
            if valor not in simbolos:
                simbolos[valor] = set()
            simbolos[valor].update(siguientes)

        for simbolo, posiciones_siguientes in simbolos.items():
            nuevo_estado = frozenset(posiciones_siguientes)
            if nuevo_estado not in estados_map:
                estados_map[nuevo_estado] = f'q_{contador_estados}'
                contador_estados += 1
                estados_pendientes.append(nuevo_estado)

            nombre_nuevo_estado = estados_map[nuevo_estado]
            transiciones[nombre_estado_actual][simbolo] = nombre_nuevo_estado

    # Reorganizar transiciones al formato (estado, simbolo) -> nuevo_estado
    transiciones_final = {}
    for estado, paths in transiciones.items():
        for simbolo, destino in paths.items():
            transiciones_final[(estado, simbolo)] = destino

    estados_final = set(estados_map.values())

    # Estados finales: aquellos que incluyen la posición final #
    for estado, nombre in estados_map.items():
        if pos_final in estado:
            estados_finales.add(nombre)

    return AFD(Q=estados_final,
               A=alfabeto,
               T=transiciones_final,
               q0='q_0',
               F=estados_finales)

def min_afd(afd: AFD) -> AFD: 
    """
    Construye el min AFD
    """
    return None # 