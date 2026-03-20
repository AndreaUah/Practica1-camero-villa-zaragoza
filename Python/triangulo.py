# triangulo.py

def checktriangle(a, b, c):
    """
    Determina el tipo de triángulo basándose en la longitud de sus tres lados.
    Se mantiene la lógica del código original en C.
    """
    # Condición de existencia del triángulo
    if (c < a + b) and (b < a + c) and (a < c + b):
        
        # Lógica de clasificación
        if a == b and a == c:
            return "Triangulo equilatero"
        elif a == b or b == c or a == c:
            # Se mantiene la lógica original (a==b || b==c)
            return "Triangulo isosceles"
        else:
            return "Triangulo escaleno"
            
    else:
        return "No es un triangulo"
