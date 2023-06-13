# 0x00. Python - Hello, World

This repository contains a collection of programs written in C and Python.

## C Programs

### lists.h
This is a header file that defines a singly linked list and its associated functions. The functions include:
- `print_listint`: This function takes a pointer to the head of a listint_t list as an argument and returns the number of nodes in the list. It also prints all the elements of the list.
- `add_nodeint`: This function takes a double pointer to the head of a listint_t list and an integer as arguments. It adds a new node at the beginning of the list containing the integer and returns the address of the new element, or NULL if it failed.
- `free_listint`: This function takes a pointer to the head of a listint_t list as an argument and frees the list.
- `check_cycle`: This function takes a pointer to a listint_t list as an argument and checks if the linked list has a cycle in it. It returns 0 if there is no cycle, 1 if there is a cycle.

## Python Programs

### 100-write.py
This program writes "and that piece of art is useful - Dora Korpar, 2015-10-19" to stderr and exits with status code 1.

### 102-magic_calculation.py
This program returns the result of 98 + (a ** b) for given values of a and b.

### 4-print_hexa.py
This program prints all numbers from 0 to 98 in decimal and hexadecimal.

### 5-print_comb2.py
This program prints numbers from 0 to 99, separated by commas and spaces.

### 6-print_comb3.py
This program prints all possible different combinations of two digits, separated by commas and spaces.

### 7-islower.py
This program checks for lowercase characters.

### 8-uppercase.py
This program prints a string in uppercase followed by a new line.

### 9-print_last_digit.py
This program prints the last digit of a number.

### lists.h
This is a header file that defines prototypes for functions used in several C programs that manipulate singly linked lists.

