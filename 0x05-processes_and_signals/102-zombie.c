#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
/**
 * infinite_while - runs an infinite loop with a sleep of 1 second in each iteration.
 * Return: 0 always
 */
int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}
/**
 * main - creates 5 zombie processes.
 * Return: 0 on success
 */
int main()
{
	int i;
	pid_t j;
	
	for (i = 0; i < 5; i++)
	{
		j = fork();
		if (j > 0)
			printf("Zombie process created, PID: %d\n", i);
		else
			exit(0);
	}
	infinite_while();
	return (0);
}
