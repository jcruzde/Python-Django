#!/usr/bin/python3

# API: suma, resta, multi, div.

import sys
import operator as op


def calcular(oper, op1, op2):
    operaciones = {'suma': op.add, 'resta': op.sub, 'multi': op.mul, 'div': op.truediv}
    try:
        return operaciones[oper](op1, op2)
    except ZeroDivisionError:
        sys.exit(['ERROR: NO PUEDO DIVIDIR ENTRE CERO'])
    except KeyError:
        sys.exit(['ERROR: TIPO DE OPERACIÓN INVÁLIDA'])


def tipo_correcto(num):
    # Devuelve num en función del tipo que sea (int o float).
    resto = num % 1
    if resto == 0:
        return int(num)
    else:
        return num


def main():
    try:
        num1 = tipo_correcto(float(sys.argv[2]))
        num2 = tipo_correcto(float(sys.argv[3]))
    except ValueError:
        sys.exit(['ERROR: SUMANDOS INCORRECTOS'])

    operacion = sys.argv[1]
    resultado = tipo_correcto(float(calcular(operacion, num1, num2)))
    print(resultado)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(['ERROR: Nº DE ARGUMENTOS INCORRECTO'])
    main()
