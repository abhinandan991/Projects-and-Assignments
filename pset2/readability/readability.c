#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main (void)
{
    string text = get_string("Text:");
    
    // Counting no. of words, letters and sentences in provided text.
    int l = 0, w = 1, s = 0; 
    
    for (int i = 0; i < strlen(text); i++)
    {
        // Counting letters
        if (isalpha(text[i]))
        {
            l++;
        }
        // Counting words
        if (isspace(text[i]))
        {
            w++;
        }
        // Counting sentences
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            s++;
        }
    }
    
    // Calculating no. of letters and sentences per 100 words.
    float L = ((l*100)/w);
    float S = ((s*100)/w);
    
    // Calculating grade index
    float index = (((0.0588 * L) - (0.296 * S) - 15.8));
    // Rounding to nearest integer
    int inx = index + 0.5;
    // Printing Grades
    if (index<1)
    {
        printf("Before Grade 1\n");
    }
    else if (index>16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", inx);
    }
}