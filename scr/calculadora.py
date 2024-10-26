def sumar(a, b):
    """
    Suma dos números.

    Args:
        a (float): El primer número.
        b (float): El segundo número.

    Returns:
        float: La suma de a y b.
    
    Example:
        >>> sumar(2, 3)
        5
    """
    return a + b

def restar(a, b):
    """
    Resta el segundo número del primero.

    Args:
        a (float): El minuendo.
        b (float): El sustraendo.

    Returns:
        float: La diferencia entre a y b.
    
    Example:
        >>> restar(5, 2)
        3
    """
    return a - b

def multiplicar(a, b):
    """
    Multiplica dos números.

    Args:
        a (float): El primer número.
        b (float): El segundo número.

    Returns:
        float: El producto de a y b.
    
    Example:
        >>> multiplicar(4, 5)
        20
    """
    return a * b

def dividir(a, b):
    """
    Divide el primer número por el segundo.

    Args:
        a (float): El numerador.
        b (float): El denominador.

    Raises:
        ValueError: Si el denominador es cero.

    Returns:
        float: El cociente de a y b.
    
    Example:
        >>> dividir(10, 2)
        5.0
    """
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b
