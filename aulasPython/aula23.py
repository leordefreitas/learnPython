"""
Dados x e E reais, E > 0, calcular uma aproximação para sen x através da
seguinte série infinita

sen x = x/(1!) - (x**3)/(3!) + (x**5)/(5!) -...+((-1)**k)*(x**(2*k+1))/((2*k+1)!)
    
      incluindo todos os termos até que

modulo(x**(2*k+1))/((2*k+1)!) < E

     Compare com os resultados de sua calculadora! 
"""

x = float(input("Digite o valor de x: "))
e = int(input("Digite o valor de e: "))
senx = 0

from math import factorial
from math import sin

for i in range(1, e+1):
	senx += (-1**i)*(x**(2*(i+1)))/(factorial(2*(i+1)))
print("A comparação dos resultados é %.5g e %.5g."%(senx, (sin(x))))

