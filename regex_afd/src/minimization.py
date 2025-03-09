from collections import defaultdict
from typing import Set, Dict, Tuple
from model.afd import AFD 

def minAFD(afd: AFD) -> AFD:
    """
    Minimiza un AFD utilizando el algoritmo de minimización de particiones (Hopcroft).

    Parámetros:
        afd (AFD): Un autómata finito determinista.

    Retorna:
        AFD: Un AFD minimizado.
    """
    # Extraer información del AFD
    Q = set(afd.Q)  
    A = set(afd.A)  
    q0 = afd.q0  
    F = set(afd.F)  
    T = afd.T  

    # Crear la función de transición `delta`
    delta = {state: {} for state in Q}
    for (q, a), q_prime in T.items():
        delta[q][a] = q_prime

    P = [F.copy(), Q - F]  
    P_nueva = []

    while True:
        P_nueva = []
        for grupo in P:
            transiciones_grupo = defaultdict(set)

            for estado in grupo:
                # Clave de la partición: cómo transiciona a otras particiones
                key = tuple(
                    next((i for i, p in enumerate(P) if delta[estado].get(a) in p), -1) for a in A
                )
                transiciones_grupo[key].add(estado)

            P_nueva.extend(transiciones_grupo.values())


        if P_nueva == P:
            break
        P = P_nueva

    estado_equivalente = {}
    for i, grupo in enumerate(P):
        estado_representante = next(iter(grupo))  
        estado_equivalente.update({estado: f"P{i}" for estado in grupo})

    min_Q = set(estado_equivalente.values())
    min_q0 = estado_equivalente[q0]
    min_F = {estado_equivalente[state] for state in F}

    min_T = {}
    for estado in estado_equivalente:
        min_estado = estado_equivalente[estado]
        for simbolo in A:
            if simbolo in delta[estado]:
                min_T[(min_estado, simbolo)] = estado_equivalente[delta[estado][simbolo]]

    return AFD(
        Q=min_Q,
        A=A,
        T=min_T,
        q0=min_q0,
        F=min_F
    )