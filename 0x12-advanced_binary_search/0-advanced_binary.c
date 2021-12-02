#include "search_algos.h"

/**
 * recursive_binary - recursive part of the binary search
 *
 * @array: the array to search in
 * @start: start index
 * @end: end index
 * @value: value to search for
 *
 * Return: first index to value
 */

int recursive_binary(int *array, size_t start, size_t end, int value)
{
	size_t mid, i;

	mid = (start + end) / 2;
	i = start;

	printf("Searching in array: ");
	while (i <= end)
	{
		printf("%d", array[i]);
		if (i != end)
			printf(", ");
		i++;
	}
	printf("\n");

	if (value == array[mid] && array[mid - 1] != value)
		return (mid);
	else if (start >= end)
		return (-1);
	else if (value > array[mid])
		return (recursive_binary(array, mid + 1, end, value));
	else if (value <= array[mid])
		return (recursive_binary(array, start, mid, value));

	return (-1);
}

/**
 * advanced_binary - binary search algorithm
 *
 * @array: the array to search in
 * @size: number of elements in the array
 * @value: value to search for
 *
 * Return: the first index where value is located if found, -1 if not found
 **/

int advanced_binary(int *array, size_t size, int value)
{
	size_t start = 0, end = size - 1;

	if (array && size > 0)
		return (recursive_binary(array, start, end, value));
	return (-1);
}
