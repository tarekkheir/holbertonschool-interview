#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{    
    listint_t *cell = malloc(sizeof(cell));
	listint_t *cur = *head;

	if (cell == NULL)
		return (NULL);
    
    cell->n = number;
    
    if (*head == NULL)
        return (cell);
    
    if (number < cur->n)
    {
        cell->next = cur;
        *head = cell;
    }
    else
    {
        while (cur->next != NULL && cur->next->n < number)
        {
            cur = cur->next;
        }

        cell->next = cur->next;
        cur->next = cell;
        
    }

	return (cell);
}
