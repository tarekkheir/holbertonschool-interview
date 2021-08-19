#include "sandpiles.h"

/**
 * print_grid - Print 3x3 grid
 * @grid: 3x3 grid
 */

static void print_grid(int grid[3][3])
{
	int i, j;

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			if (j)
				printf(" ");
			printf("%d", grid[i][j]);
		}
		printf("\n");
	}
}

/**
 * chek_stable - check if sandpile is stable
 * @grid: sandpile to check
 * Return: 1 if sandpile is stable or 0
 */

int check_stable(int grid[3][3])
{
	int i, j = 0;

	while (j < 3)
	{
        i = 0;
		while (i < 3)
		{
			if (grid[j][i] > 3)
				return (0);
            i++;
		}
        j++;
	}
	return (1);
}


/**
 * topple_pile - make the sandpile stable
 * @grid1: sandpile
 * @grid2: empty grid
 */

void topple_pile(int grid1[3][3], int grid2[3][3])
{
	int x, y;

	for (x = 0; x < 3; x++)
	{
		for (y = 0; y < 3; y++)
		{
			if (grid1[x][y] > 3)
			{
				grid2[x][y] += grid1[x][y] - 4;
				if (x - 1 >= 0)
					grid2[x - 1][y] += 1;
				if (x + 1 < 3)
					grid2[x + 1][y] += 1;
				if (y - 1 >= 0)
					grid2[x][y - 1] += 1;
				if (y + 1 < 3)
					grid2[x][y + 1] += 1;
			}
			else
				grid2[x][y] += grid1[x][y];
		}
	}
}


/**
 * sandpiles_sum - computes the sum of two sandpiles
 * @grid1: Left 3x3 grid
 * @grid2: Right 3x3 grid
 */

void sandpiles_sum(int grid1[3][3], int grid2[3][3])
{
	int x, y;

	for (x = 0; x < 3; x++)
	{
		for (y = 0; y < 3; y++)
			grid1[x][y] = grid1[x][y] + grid2[x][y];
	}

	while (check_stable(grid1) != 1)
	{
		for (x = 0; x < 3; x++)
		{
			for (y = 0; y < 3; y++)
				grid2[x][y] = 0;
		}

		printf("=\n");
		topple_pile(grid1, grid2);
		print_grid(grid1);

		for (x = 0; x < 3; x++)
		{
			for (y = 0; y < 3; y++)
			{
				grid1[x][y] = grid2[x][y];
			}
		}
	}
}
