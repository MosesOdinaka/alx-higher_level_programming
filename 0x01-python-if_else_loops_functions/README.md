# 0x01. Python - if/else, loops, functions

This repository contains a collection of programs written in C and Python.

## C Programs

### lists.h
This is a header file that defines a singly linked list and its associated functions. The functions include:
- `print_listint`: This function takes a pointer to the head of a listint_t list as an argument and returns the number of nodes in the list. It also prints all the elements of the list.
- `add_nodeint_end`: This function takes a double pointer to the head of a listint_t list and an integer as arguments. It adds a new node at the end of the list containing the integer and returns the address of the new element, or NULL if it failed.
- `free_listint`: This function takes a pointer to the head of a listint_t list as an argument and frees the list.
- `insert_node`: This function takes a double pointer to the head of a sorted singly-linked list and an integer as arguments. It inserts a new node containing the integer into the list at the correct position and returns a pointer to the new node, or NULL if it failed.

## Python Programs

### 0-positive_or_negative.py
This program assigns a random signed number to variable number each time it is executed and prints whether it is positive, negative, or zero.

### 100-print_tebahpla.py
This program prints the alphabet in reverse order, alternating upper- and lower-case.

### 101-remove_char_at.py
This program takes a string and an index as arguments and creates a copy of the string without the character at that position.

### 102-magic_calculation.py
This program matches bytecode provided by Holberton School. It takes three integers as arguments and returns c if a is less than b, otherwise it returns (a + b) if c is greater than b, otherwise it returns (a * b - c).

### 10-add.py
This program takes two integers as arguments and returns their sum.

### 11-pow.py
This program takes two integers as arguments and returns the first raised to the power of the second.

### 12-fizzbuzz.py
This program prints numbers from 1 to 100 separated by spaces. For multiples of three, it prints Fizz instead of the number. For multiples of five, it prints Buzz instead of the number. For multiples of both three and five, it prints FizzBuzz instead of the number.

### 1-last_digit.py
This program assigns a random signed number to variable number each time it is executed and prints its last digit.

### 2-print_alphabet.py
This program prints the alphabet in lowercase, not followed by a new line.

### 3-print_alphabt.py
This program prints the alphabet in lowercase except for q and e, not followed by a new line.

### 4-print_hexa.py
This program prints numbers from 0 to 98 in decimal and hexadecimal.

### 5-print_comb2.py
This program prints numbers from 0 to 99 separated by commas and spaces.

### 6-print_comb3.py
This program prints all possible different combinations of two digits in ascending order. The two digits must be different - 01 and 10 are considered identical.

### 7-islower.py
This program checks for lowercase characters.

### 8-uppercase.py
This program takes a string as an argument and prints it in uppercase followed by a new line.

### 9-print_last_digit.py
This program takes an integer as an argument, prints its last digit, and returns it.

