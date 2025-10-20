# Atividade: Implementação de Fatorial em Python

## Objetivo
O objetivo desta atividade é implementar a função de cálculo de fatorial de um número natural `n` em **Python**, utilizando três abordagens diferentes:

1. **Método Iterativo**
2. **Método Recursivo**
3. **Método Recursivo com uso de `functools.lru_cache`**

Ao final, os alunos devem compreender:
- As diferenças conceituais entre iteração e recursão;
- As limitações práticas da recursão em Python (profundidade de pilha);
- O funcionamento e a utilidade do mecanismo de *memoization* (`lru_cache`).

---

## Definição do Problema
Dado um número inteiro não negativo `n`, o fatorial é definido como:

 n! = n × (n-1) × (n-2) × ... × 2 × 1
 
 Com a convenção de que:
0! = 1


---

## Tarefas

### 1. Implementação Iterativa
- Implemente uma função `fatorial_iterativo(n)` que calcule o fatorial utilizando um laço `for`.
- Avalie sua eficiência e explique por que não há risco de `RecursionError` nesta abordagem.

### 2. Implementação Recursiva
- Implemente uma função `fatorial_recursivo(n)` que calcule o fatorial utilizando chamadas recursivas.
- Garanta que exista um **caso base** (ex.: `n == 0` ou `n == 1`).
- Teste com valores pequenos e discuta o que acontece ao usar valores grandes (`RecursionError`).

### 3. Implementação com `lru_cache`
- Implemente uma função `fatorial_lru(n)` decorada com `@functools.lru_cache(maxsize=None)`.
- Verifique se os resultados são corretos e compare com a versão recursiva simples.
- Explique se houve ganho de desempenho no caso do fatorial e por quê.

---

## Exemplos de Uso

```python
print(fatorial_iterativo(5))   # 120
print(fatorial_recursivo(5))   # 120
print(fatorial_lru(5))         # 120
