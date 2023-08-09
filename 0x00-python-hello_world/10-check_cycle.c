#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *now, *tmp;

	if (list == NULL || list->next == NULL)
		return (0);
	now = list;
	tmp = now->next;

	while (now && tmp && tmp->next)
	{
		if (now == tmp)
			return (1);
		now = now->next;
		tmp = tmp->next->next;
	}
	return (0);
}
