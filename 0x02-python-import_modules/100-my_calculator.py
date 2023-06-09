#!/usr/bin/python3
"""
This script imports functions from calculator_1.py
and performs basic arithmetic operations.

Usage: ./100-my_calculator.py <a> <operator> <b>
where <a> and <b> are integers and <operator> is
one of +, -, * or /.
"""
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':
    import sys

    args = sys.argv
    if len(args) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(args[1])
    b = int(args[3])
    operator = args[2]

    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    elif operator == '/':
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{} {} {} = {}".format(a, operator, b, result))
