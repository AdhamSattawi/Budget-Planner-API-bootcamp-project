# This function solve a quadratic equation


def quadratic(a: int, b: int, c: int) -> str:
    x2: float = (-b + ((b**2) - (4 * a * c)) ** 0.5) / (2 * a)
    x1: float = (-b - ((b**2) - (4 * a * c)) ** 0.5) / (2 * a)
    return f"x1 ={x1: .2f}, x2 ={x2: .2f}"


print(quadratic(-3, -5, -7))
