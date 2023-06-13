##0x03. Python - Data Structures: Lists, Tuples

This file contains a collection of programs written in C and Python.

## C Programs

### lists.h
This is a header file that defines a singly linked list and its associated functions. The functions include:
- `print_listint`: This function takes a pointer to the head of a listint_t list as an argument and returns the number of nodes in the list. It also prints all the elements of the list.
- `add_nodeint_end`: This function takes a double pointer to the head of a listint_t list and an integer as arguments. It adds a new node at the end of the list containing the integer and returns the address of the new element, or NULL if it failed.
- `free_listint`: This function takes a pointer to the head of a listint_t list as an argument and frees the list.
- `is_palindrome`: This function takes a pointer to the head of a singly linked list of integers as an argument and returns 1 if the linked list is a palindrome, and 0 otherwise.

## Python Programs

### 0-print_list_integer.py
This program takes a list of integers as an argument and prints all integers of the list, one per line.

### 1-element_at.py
This program takes a list and an index as arguments and retrieves an element from the list at that index. If idx is negative or out of range, it returns None.

### 2-replace_in_list.py
This program takes a list, an index, and an element as arguments. It substitutes the element at that index in the list with the new element. If idx is negative or out of range, it returns the original list.

### 3-print_reversed_list_integer.py
This program takes a list of integers as an argument and prints all integers of the list in reverse order, one per line.

### 4-new_in_list.py
This program takes a list, an index, and an element as arguments. It replaces an element in a copied version of the original list at that specific position with the new element. If idx is negative or out of range, it returns the original list.

### 5-no_c.py
This program takes a string as an argument and returns a new string where all characters c and C have been removed.

### 6-print_matrix_integer.py
This program takes a matrix of integers as an argument and prints it.

### 7-add_tuple.py
This program takes two tuples as arguments and returns a new tuple where each element is the sum of the elements at that position in each tuple. If a tuple is smaller than 2, its missing elements are considered to be 0.

### 8-multiple_returns.py
This program takes a sentence as an argument and returns a tuple with its length and its first character. If sentence is empty, its first character should be equal to None.

### 10-divisible_by_2.py
This program takes a list of integers as an argument and finds all multiples of 2 in it. It returns a new list with True or False, depending on whether each integer in my_list is divisible by 2 or not.

### 11-delete_at.py
This program takes a list and an index as arguments. It deletes the item at that specific position in my_list. If idx is negative or out of range, it returns my_list unchanged.

