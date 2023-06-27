#!/usr/bin/python3
def safe_print_division(a, b):
    outcome = None
    try:
        outcome = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(outcome))
        return outcome
