#include "lists.h"

/**
 * check_cycle - check if a single linked list has a cycle or not
 * @list: single linked list
 * Return: 1 if it has a cycle, 0 if not
 */

int check_cycle(listint_t *list) {

    listint_t *slow = list;
    listint_t *fast = list;

    if (list && list->next != NULL)
    {
        while (slow && fast && fast->next)
        {
            slow = slow->next;
            fast = fast->next->next;

            if (slow == fast)
                return (1);
        }
    }

    return (0);
}
