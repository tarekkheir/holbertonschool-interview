#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 *
 * @head: linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *lst = *head;
	int val[2048], i = 0, j = 0;

	if (*head)
	{
		while (lst)
		{
			val[i] = lst->n;
			lst = lst->next;
			i++;
		}

		while (j < i / 2)
		{
			if (val[j] == val[i - j - 1])
				j++;
			else
				return (0);
		}
	}

	return (1);
}
