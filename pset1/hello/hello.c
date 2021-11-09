#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //Getting name from user
    string answer = get_string("Enter the name:");
    printf("hello, %s\n", answer);
}