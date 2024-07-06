!pip install pulp
from pulp import *

# Definindo o problema de otimização
prob = LpProblem("Problema Simplex", LpMaximize)

# Definindo as variáveis de decisão
x1 = LpVariable("catarata", 0, None, LpInteger)
x2 = LpVariable("hernia", 0, None, LpInteger)
x3 = LpVariable("varizes", 0, None, LpInteger)
x4 = LpVariable("vesicula", 0, None, LpInteger)
x5 = LpVariable("amidalas", 0, None, LpInteger)

# Definindo a função objetivo levando em conta a incidência
# Definindo as restrições de custo e tempo
# CENÁRIO ATUAL
prob += 3.62*x1 + 10.01*x2+13.71*x3+7.36*x4+3.09*x5
prob += 800*x1 + 700*x2 + 1000*x3 + 1500*x4 + 2000*x5 <= 200000000
prob += 0.75*x1 + 2.25*x2 + 2.08*x3 + 2.13*x4 + 1.75*x5 <= 160

#simulacao 1 - MESMA INCIDÊNCIA
# prob += 1.0 * x1 + 1.0 * x2 + 1.0 * x3 + 1.0 * x4 + 1.0 * x5
# prob += 800*x1 + 700*x2 + 1000*x3 + 1500*x4 + 2000*x5 <= 200000000
# prob += 0.75*x1 + 2.25*x2 + 2.08*x3 + 2.13*x4 + 1.75*x5 <= 160

#simulacao 2 - MENOR INCIDÊNCIA É A MAIS BARATA
# prob += 3.62*x1 + 10.01*x2+13.71*x3+7.36*x4+3.09*x5
# prob += 800*x1 + 700*x2 + 1000*x3 + 1500*x4 + 100*x5 <= 200000000
# prob += 0.75*x1 + 2.25*x2 + 2.08*x3 + 2.13*x4 + 1.75*x5 <= 160

#simulacao 3 - MAIS BARATA PORÉM DEMANDA MAIS TEMPO
# prob += 3.62*x1 + 10.01*x2+13.71*x3+7.36*x4+3.09*x5
# prob += 800*x1 + 700*x2 + 1000*x3 + 1500*x4 + 2000*x5 <= 200000000
# prob += 3.00*x1 + 2.25*x2 + 2.08*x3 + 2.13*x4 + 1.75*x5 <= 160

# Resolvendo o problema
prob.solve()

# Imprimindo a solução
print("Solução ótima:")
print("x1 = ", value(x1))
print("x2 = ", value(x2))
print("x3 = ", value(x3))
print("x4 = ", value(x4))
print("x5 = ", value(x5))
print("Valor máximo da função objetivo: ", value(prob.objective))
