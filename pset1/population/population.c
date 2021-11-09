#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt for start size
    int s;
    do
    {
        s = get_int("Enter the starting population:");
    }
    while (s<9);

    // Prompt for end size
    int e;
    do
    {
        e = get_int("Enter the end size of the population:");
    }
    while (e<s);

    //Calculate number of years until we reach threshold
    int increase;
    int years = 0;
    for (int j = s; j<e; j=j+increase)
    {
        increase=(j/3)-(j/4);
        years++ ;
    }

    // TODO: Print number of years
    printf("Years: %i\n", years);
}