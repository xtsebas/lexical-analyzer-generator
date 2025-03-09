#referencia a https://github.com/xtsebas/regex_to_AFD/blob/main/Model/Estructuras/Stack.py
class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        """
        Inserta un item en el stack
        """
        self.items.append(item)
    
    def pop(self):
        """
        Elimina y devuelve el ultimo elemento en la pila
        Si la pila esta vacio devuelve None
        """
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
    
    def peek(self):
        """
        Devuelve el ultimo elemento en la pila sin eliminarlo
        Si la pila esta vacio devuelve None
        """
        if not self.is_empty():
            return self.items[-1]
        else:
            return None
        
    def is_empty(self):
        return len(self.items) == 0