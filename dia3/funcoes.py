def soma(x: int | float, y: int | float) -> int |  float:
    """Soma x + y e retorna o resultado"""
    return x + y

def print_subtracao(x: int | float, y: int | float) -> int | float:
    """Subtrai x - y e imprime o resultado (sem retorno)"""
    print(f"{x - y}")

def soma_sem_parametro() -> int | float:
    """Soma x + y sem parâmetros e retorna o resultado"""
    x = 5
    y = 5
    return x + y

def multiplicacao(x: int | float, y: int | float) -> int | float:
    """Multiplica x * y e retorna o resultado"""
    return x * y