"""mypackage 包中的数学工具模块"""


def add(x: float, y: float) -> float:
    """加法"""
    return x + y


def subtract(x: float, y: float) -> float:
    """减法"""
    return x - y


def multiply(x: float, y: float) -> float:
    """乘法"""
    return x * y


def divide(x: float, y: float) -> float:
    """除法"""
    return x / y


if __name__ == '__main__':
    print(f"add(2,3) = {add(2, 3)}")
    print(f"multiply(4,5) = {multiply(4, 5)}")
