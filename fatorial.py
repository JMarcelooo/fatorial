#!/usr/bin/env python3
"""
fatorial.py

Template de implementação para cálculo do fatorial em Python.
Os alunos devem implementar as três abordagens abaixo:

1. Método Iterativo
2. Método Recursivo
3. Método Recursivo com uso de functools.lru_cache
"""

import functools


# ---------------------------
# Implementação Iterativa
# ---------------------------
def fatorial_iterativo(n: int) -> int:
    if n < 0:  
        print("erro")
    
    resultado = 1
    for i in range(1, n + 1 ):
        resultado = resultado * i

    return resultado


# ---------------------------
# Implementação Recursiva
# ---------------------------
def fatorial_recursivo(n: int) -> int:
            """Calcula o fatorial de n de forma recursiva"""
            if n == 0:
                return 1
            if n > 0:
                return n * fatorial_recursivo(n-1)
            if n < 0:
                print("erro")
        
    


# ---------------------------
# Implementação com LRU Cache
# ---------------------------
@functools.lru_cache(maxsize=None)
def fatorial_lru(n: int) -> int:
    """Calcula o fatorial de n com recursão + memoização (lru_cache)."""
    # TODO: Implementar igual ao recursivo, mas com o decorador @lru_cache
    if n == 0:
        return 1
    if n > 0:
        return n * fatorial_recursivo(n-1)
    if n < 0:
        print("erro")
    pass


# ---------------------------
# Função Principal (testes)
# ---------------------------
if __name__ == "__main__":
    numero = 5  # valor de exemplo; pode ser alterado

    print(f"Iterativo: {numero}! = {fatorial_iterativo(numero)}")
    print(f"Recursivo: {numero}! = {fatorial_recursivo(numero)}")
    print(f"LRU Cache: {numero}! = {fatorial_lru(numero)}")
