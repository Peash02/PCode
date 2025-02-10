import sympy as sp

# Define the matrix A
A = sp.Matrix([[2, 0, 1],
               [0, 2, 0],
               [1, 0, 2]])

# Define the variable for eigenvalues
λ = sp.symbols('λ')

# Calculate the characteristic polynomial
char_poly = A.charpoly(λ)
char_pol