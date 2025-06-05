"""
Модуль для выполнения математических операций
"""

def add(a, b):
    """Сложение"""
    return a + b

def subtract(a, b):
    """Вычитание"""
    return a - b

def multiply(a, b):
    """Умножение"""
    return a * b

def divide(a, b):
    """Деление"""
    if b == 0:
        raise ValueError("Деление на ноль невозможно!")
    return a / b

# Словарь операций
OPERATIONS = {
    'add': add,
    'subtract': subtract,
    'multiply': multiply,
    'divide': divide
}

def calculate(operation, num1, num2):
    """
    вычисление на основе переданной операции
    
    Args:
        operation (str): Название операции ('add', 'subtract', 'multiply', 'divide')
        num1 (float): Первое число
        num2 (float): Второе число
    
    Returns:
        float: Результат вычисления
    """
    if operation not in OPERATIONS:
        raise ValueError(f"Неизвестная операция: {operation}")
    
    return OPERATIONS[operation](num1, num2)