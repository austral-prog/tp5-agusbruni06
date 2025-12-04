# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante > 0:
        r1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
        r2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
        result = f"({r1}, {r2})"
        return result
    elif discriminante == 0:
        r1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
        r2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
        result = f"({r1})"
        return result
    else:
        result = "( )"
        return result
   
    #result = f"({r1}, {r2})"
    #return result

A = int(input("ingrese parametro a: "))
B = int(input("ingrese parametro b: "))
C = int(input("ingrese parametro c: "))
print(roots(A, B, C))


def value_y(a, b, c, x):
    valory = a*x**2 + b*x + c
    return valory

ejex = int(input("ingrese valor de x: "))
print(value_y(A, B, C, ejex))

def to_string(a, b, c):
    ecuacion1 = f"f(x) = {a}X^2 + {b}X + {c}"
    return ecuacion1
print(to_string(A, B, C))


def derivation(a, b, c):
    ecuacion2 = f"f'(x) = {2*a}x + {b} + {c*0}"
    return ecuacion2
print(derivation(A, B, C))
