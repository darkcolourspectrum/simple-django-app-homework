from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from calc_operations import *

def index(request):
    """
    Главная страница с формой калькулятора
    """
    return render(request, 'calculator/index.html')

@csrf_exempt
def calculate_result(request):
    """
    Обработка AJAX запроса для вычисления результата
    """
    if request.method == 'POST':
        try:
            if request.content_type == 'application/json':
                data = json.loads(request.body)
                num1 = float(data.get('num1', 0))
                num2 = float(data.get('num2', 0))
                operation = data.get('operation', '')
            else:
                num1 = float(request.POST.get('num1', 0))
                num2 = float(request.POST.get('num2', 0))
                operation = request.POST.get('operation', '')

            result = calculate(operation, num1, num2)
            
            operation_symbols = {
                'add': '+',
                'subtract': '-',
                'multiply': '×',
                'divide': '÷'
            }
            
            operation_names = {
                'add': 'Сложение',
                'subtract': 'Вычитание',
                'multiply': 'Умножение',
                'divide': 'Деление'
            }
            
            symbol = operation_symbols.get(operation, '?')
            name = operation_names.get(operation, 'Неизвестная операция')
            
            return JsonResponse({
                'success': True,
                'result': result,
                'num1': num1,
                'num2': num2,
                'operation': operation,
                'operation_symbol': symbol,
                'operation_name': name,
                'expression': f"{num1} {symbol} {num2} = {result}"
            })
            
        except ValueError as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': f'Произошла ошибка: {str(e)}'
            })
    
    return JsonResponse({
        'success': False,
        'error': 'Метод не поддерживается'
    })