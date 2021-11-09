// Implements a dictionary's functionality

#include <stdbool.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <strings.h>
#include <ctype.h>

#include "dictionary.h"


// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = 10000;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    //making copy of word
    int n = strlen(word);
    char word_copy[LENGTH + 1];
    for (int i = 0; i < n; i++)
    {
        word_copy[i] = tolower(word[i]);
    }
    // Adds null terminator to end string
    word_copy[n] = '\0';
    
    //hashing word copy
    unsigned int h=hash(word_copy);
    //set node cursor to required head
    node *cursor = table[h];
    //comparing
    for(node *temp=cursor; temp!=NULL;temp=temp->next)
    {
        //if word in dictionary
        if ((strcasecmp(temp->word,word_copy))==0)
        {
            return true;
        }
    }
    // Cursor has reached end of list and word has not been found in dictionary so it must be misspelled
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    unsigned int hash = 0;
    for (int i = 0, n = strlen(word); i < n; i++)
    {
        hash = (hash << 2) ^ word[i];
    }
    return hash % N;
}
//word counter initiated(counted in load function)
int wc=0;

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    //open dictionary
    FILE *dic=fopen(dictionary,"r");
    if (dic==NULL)
    {
        return false;
    }
    
    
    char word[LENGTH+1];
    while (fscanf(dic, "%s", word)!=EOF)
    {
        
        //creating the new node
        node *n=malloc(sizeof(node));
        if(n==NULL)
        {
            unload();
            return false;
        }
        strcpy(n->word,word);
        n->next=NULL;
        
        //hashing
        unsigned int h=hash(n->word);
        
        //inserting into linked list
        node *head=table[h];
        //if first word in index(no collision)
        if (head==NULL)
        {
            table[h]=n;
            wc++;
        }
        //handling collisions
        else
        {
            n->next=table[h];
            table[h]=n;
            wc++;
        }
    }
    //closing dictionary
    fclose(dic);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return wc;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    //traversing all indexes in hash table
   for (int i = 0; i < N; i++)
   {
       node *head = table[i];
       node *cursor = head;
       // freeing linked lists
       while (cursor != NULL)
       {
           node *temp = cursor;
           cursor = cursor->next;
           free(temp);
        }
    }
    return true;
}

