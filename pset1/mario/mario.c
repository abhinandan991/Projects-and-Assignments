#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // Getting required input and verifying if requirements are satisfied
    int n;
    do
    {
        n = get_int("Enter the size of the pyramid:");
    }
    while ((n<1) || (n>8));
    
    // Generating pyramid
    for (int i=1; i<=n; i++)
    {
        // Printing leading spaces
        for (int j=n; j>i; j--)
        {
            printf(" ");
        }
        // Printing #
        for (int h=0; h<i; h++)
        {
            printf("#");
        }
        //Printing middle gap
        printf("  ");
        //Printing #
        for (int h=0; h<i; h++)
        {
            printf("#");
        }
        printf("\n");
    }
    
}