import numpy as np
import matplotlib.pyplot as plt
from sympy.solvers import solve
from sympy import symbols, Eq, solve

#Hallar los puntos de corte

x, y = symbols("x y")
equation_1 = Eq((3*x + 7), y)
equation_2 = Eq((x - y), 5)
equation_3 = Eq((x + y), 5)

equx1 =  solve((equation_1),(x,y))
equy1 =  solve((equation_1),(y,x))
equx1 = equx1[0][0]
equy1 = equy1[0][0]

def funcion(x):
   # Despejamos la y en la ecuación 20x+30y=30
   return (30-20*x)/30

X = []
Y = []
for x in range(20):
   y = funcion(x)
   X.append(x)
   Y.append(y)

plt.plot(X, Y)
plt.show()

solx1 = (solve(equx1, y))
soly1 = (solve(equy1, x))

puntos1 = solx1+soly1

equx2 =  solve((equation_2),(x,y))
equy2 =  solve((equation_2),(y,x))
equx2 = equx2[0][0]
equy2 = equy2[0][0]

solx2 = (solve(equx2, y))
soly2 = (solve(equy2, x))

puntos2 = solx2+soly2

equx3 =  solve((equation_3),(x,y))
equy3 =  solve((equation_3),(y,x))
equx3 = equx3[0][0]
equy3 = equy3[0][0]

solx3 = (solve(equx3, y))
soly3 = (solve(equy3, x))

puntos3 = solx3+soly3

print(puntos1)
print(puntos2)
print(puntos3)





