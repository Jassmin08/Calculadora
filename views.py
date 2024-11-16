from django.shortcuts import render

def calculadora(request):
    resultado = None
    if request.method == "POST":
        try:
            num1 = float(request.POST.get('num1'))
            num2 = float(request.POST.get('num2'))
            operacion = request.POST.get('operacion')

            if operacion == 'suma':
                resultado = num1 + num2
            elif operacion == 'resta':
                resultado = num1 - num2
            elif operacion == 'multiplicacion':
                resultado = num1 * num2
            elif operacion == 'division':
                if num2 != 0:
                    resultado = num1 / num2
                else:
                    resultado = "Error: División por cero"
            else:
                resultado = "Operación no válida"
        except ValueError:
            resultado = "Por favor, ingrese valores numéricos válidos"

    return render(request, 'calculadora/calculadora.html', {'resultado': resultado})
