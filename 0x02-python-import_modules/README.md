# Python Program

This repository contains a collection of Python scripts that demonstrate basic arithmetic operations and command line argument handling.

## Usage

Each script can be run from the command line by navigating to the directory containing the script and running `python3 <script_name>.py`.

For example, to run the script that performs basic arithmetic operations using functions imported from `calculator_1.py`, navigate to the directory containing the script and run `python3 100-my_calculator.py <a> <operator> <b>` where `<a>` and `<b>` are integers and `<operator>` is one of `+`, `-`, `*` or `/`.

## Scripts

- `add_0.py`: Contains a function that adds two integers. The function takes two arguments, `a` and `b`, and returns their sum.
- `calculator_1.py`: Contains functions that perform addition, subtraction, multiplication, and division on two integers. Each function takes two arguments, `a` and `b`, and returns the result of the corresponding operation.
- `100-my_calculator.py`: Imports functions from `calculator_1.py` and performs basic arithmetic operations based on command line arguments. The script takes three arguments: two integers `<a>` and `<b>`, and an operator `<operator>` which is one of `+`, `-`, `*` or `/`. The script then performs the corresponding operation on `<a>` and `<b>` using the imported functions from `calculator_1.py` and prints the result.
- Other scripts demonstrate handling command line arguments and printing the results.

## Requirements

- Python 3
- No additional dependencies are required.
