def dividir(num1, num2):
    try:
        resultado = num1 / num2
    except ZeroDivisionError as e:
        print(e)

print(dividir(5,0))