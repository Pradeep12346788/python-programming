import cmath  

def solve_quadratic(a, b, c):
    discriminant = cmath.sqrt(b**2 - 4*a*c)
    
    root1 = (-b + discriminant) / (2*a)
    root2 = (-b - discriminant) / (2*a)
    
    return root1, root2

a = 2
b = -4
c = 5

roots = solve_quadratic(a, b, c)
print("Root 1:", roots[0])
print("Root 2:", roots[1])
