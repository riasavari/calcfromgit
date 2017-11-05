def add(a, b):
    """ performs addition   """
    return a + b


def subtract(a, b):
    """ performs subtraction   """
    return a - b


def multiply(a, b):
    """ performs multiplication   """
    return a * b


def divide(a, b):
    """ performs division   """
    if b == 0:
        raise ValueError("Can not divide by zero!")
    return a / b
