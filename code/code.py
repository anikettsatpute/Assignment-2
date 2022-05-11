#CS21BTECH11056

from sympy import symbols , Eq , solve


x , y = symbols( 'x , y' )

#declaring equations
eq1 = Eq( (9*x - 4*y) , 22 )
eq2 = Eq( y , 14)

#solving the equations
print( solve(eq1 , eq2) , ( x , y))
