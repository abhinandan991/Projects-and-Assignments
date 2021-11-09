#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    char key[26] ;
    
    //Checking validity of commandline argument
    if (argc!=2)
    {
        //Error if invalid number of arguments have been provided
        printf("Usage: ./substitution\n");
        return 1;
    }
    if (strlen(argv[1])!=26)
    {
        //Error if Key does not contain 26 characters
        printf("Key must have 26 characters.\n");
        return 1;
    }
    //Checking if key provided is valid
    for (int h=0; h<26; h++)
    {
        for (int y=(h+1); y<26; y++)
        {
            //Checking for repeatation in key
            if (argv[1][h]==argv[1][y])
            {
                //Error since key cannot contain repeating characters
                printf("Key cannot have repeating characters.\n");
                return 1;
            }
        }
        if (isalpha(argv[1][h])==0)
        {
            //Error since key cannot contain digits
            printf("Key cannot have digits.\n");
            return 1;
        }
        char c=argv[1][h];
        key[h]=c;
    }
    
    //Inputting text to be encrypted
    string ptext=get_string("plaintext: ");
    int length=strlen(ptext);
    char text[length];
    //Encrypting
    for (int i=0; i<length; i++)
    {
        //Copy as is if character is non alphabetical
        if (isalpha(ptext[i])==0)
        {
            text[i]=ptext[i];
            continue;
        }
        for (int j=65,h=0; j<91; j++,h++)
        {
            if ((ptext[i]==j) || (ptext[i]==(j+32)))
            {
                //Converting to uppercase or lowercase as per given text to be encrypted conserving the case of the text
                if (isupper(ptext[i])!=0)
                {
                    text[i]=toupper(key[h]);
                }
                else if (islower(ptext[i])!=0)
                {
                    text[i]=tolower(key[h]);
                }
            }
        }
    }
    
    //Output
    printf("ciphertext: ");
    for (int g=0; g<length; g++)
    {
        printf("%c", text[g]);
    }
    printf("\n");
    return 0;
}