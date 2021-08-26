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
	listint_t *size = *head;
	int i = 0;
    int j = 0;
    int tab[512];

    if (*head != NULL)
    {
        while (size)
        {
            tab[i] = size->n;
            size = size->next;
            i++;
        }

        while (j < i / 2)
        {
            if (tab[j] == tab[i - j - 1])
                j++;
            else
                return (0);
        }
    }

    return (1);
}
