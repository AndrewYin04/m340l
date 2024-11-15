import numpy as np
from numpy import linalg
from sympy import * 
from IPython.display import display
init_printing(pretty_print=True, use_latex=True)

#n=3
#A = Matrix(n,n,[-1,2,2,-1,-4,-2,-3,9,7])
#A = Matrix(n,n,[3.2,-2.5,5.9,-1.5,2.2,-3.9,-2.1,2.1,-4.4])
n=5
#A = Matrix(n,n,[5.0,0,-2,0,6,0,5,-2,2,0,5,-5,4,4,4,2,6,-5,-6,0,1,-5,1,-2,2])
A = randMatrix(n,n,-6,6)
display(A)
L=A.eigenvects()
for i in range (0,n):
    display(L[i][0].evalf())
#display(L)

# Power Method
xzero=zeros(n,1)
xzero[0]=1.0
xn=xzero
for i in range (0,10):
    xn=A*xn
    #display(xn) #This is to confirm I'm grabbing the correct entry in the upcoming for loop
    evalest=xn[0]
    #This for loop is how Lay extracts the estimated eigenvalue
    for i in range (0,n):
        if abs(xn[i])>abs(evalest):
            evalest=xn[i]
    xn=xn/evalest
    display(evalest) #These next two lines allow you to display the iterates as you go.  Delete for speed.
    display(xn)
#display(xn)
#display(evalest)

# Inverse Power Method
alpha=0
xzero=zeros(n,1)
xzero[0]=1.0
xn=xzero
for i in range (0,40):
    C=(A-alpha*eye(n)).col_insert(n,xn)
    Red=Matrix.rref(C,pivots=false)
    xn=Red[:,n]
    #The following is the method of getting eigenvalues from Lay
    mu=xn[0]
    for i in range (0,n):
        if abs(xn[i])>abs(mu):
            mu=xn[i]
    xn=xn/mu
    nu=alpha+1/mu
    #display(xn)
    #display(nu)
display(xn)
display(nu)

