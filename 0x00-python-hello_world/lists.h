#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct list_int - the singly linked list
 * @index: the integer
 * @next: the pointer to the next node
 * Description: singly linked list node structure.
 */
typedef struct list_int
{
	int index;
	struct list_int *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int index);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif
