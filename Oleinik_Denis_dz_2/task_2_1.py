"""
Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем. После выполнения вычисления программа не
должна завершаться, а должна запрашивать новые данные для вычислений. Завершение
программы должно выполняться при вводе символа '0' в качестве знака операции. Если
пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об
ошибке и снова запрашивать знак операции. Также сообщать пользователю о невозможности
деления на ноль, если он ввел 0 в качестве делителя
"""
# https://drive.google.com/file/d/19ki-RLtNiuxUS2FVoIt2Tmt5R5k_YdY0/view?usp=sharing


def action(a, b, symbl):
    if symbl == '+':
        c = float(a) + float(b)
    elif symbl == '-':
        c = float(a) - float(b)
    elif symbl == '*':
        c = float(a) * float(b)
    elif symbl == '/':
        c = float(a) / float(b)
    return c


def isDigit(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


while True:
    a = input('Введите число "a": ')
    b = input('Введите число "b": ')
    symbl = input('Какое действие будем выполнять (+, -, * или /)? Для выхода нажмите "0": ')
    if b == '0' and symbl == '/':
        print('Делить на ноль нельзя!')
    elif isDigit(a) and isDigit(b):
        if symbl == '0':
            break
        # elif symbl == '+' or symbl == '-' or symbl == '*' or symbl == '/':
        elif symbl in '+, -, *, /':
            print('Ваше значение:', action(a, b, symbl))
            print('Повторим?!')
        # elif symbl != '+' or symbl != '-' or symbl != '*' or symbl != '/' or symbl != 0:
        # elif symbl not in '+, -, *, /, 0':
        else:
            print('Вы ввели не правильное значение. Повторите!')
    else:
        print('Вы ввели не число. Повторите!')
