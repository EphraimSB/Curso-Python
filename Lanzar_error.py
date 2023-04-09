class OperadorExcepcion(Exception):
    def __init__(self, mensaje) -> None:
        super().__init__(mensaje)

def divir(a, b):
    if b == 0:
        raise OperadorExcepcion ("Error; No se puede dividir por cero!")
    else:
        return a / b
    
divir(4, 0)