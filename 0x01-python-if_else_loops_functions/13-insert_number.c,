#include "lists.h"

/**
 * insert_node - function that inserts a number into a sorted
 * singly linked list
 * @head: head
 * @number: number
 * Return: address of the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr, *new, *prev;

	new = malloc(sizeof(listint_t));

	if (!new)
		return (0);

	new->n = number;

	if (!*head)
	{
		new->next = NULL;
		*head = new;
		return (new);
	}

	curr = *head;

	if (curr->n > number)
	{
		new->next = curr;
		*head = new;
		return (new);
	}

	while (curr->next)
	{
		if (curr->n > number)
		{
			prev->next = new;
			new->next = curr;
			return (new);
		}
		prev = curr;
		curr = curr->next;
	}
	curr->next = new;
	new->next = NULL;
	return (new);

}
