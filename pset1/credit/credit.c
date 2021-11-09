#include <stdio.h>
#include <cs50.h>

// Creating function to use Luhn's algorithm for checksum
int checksum(long n)
{
    int c = 0;
    int p1 = 0;
    int p2 = 0;
    for (long i=n ; i>0 ; i = i/10)
    {
        int x=i%10;
        if ((c%2)==0)
        {
            p1=p1+x;
        }
        else
        {
            x=(x*2);
            for (int j=x ; j>0 ; j = j/10)
            {
                int f = (j%10);
                p2=p2+(f);
            }
        }
        c=c+1;
    }
    int p3 = p1 + p2;
    if ((p3%10)==0)
    {
        // Returns 1 if checksum is satisfied
        return 1;
    }
    else
    {
        // Resturns 0 if checksum is not satisfied
        return 0;
    }
}

int main(void)
{
    long n = get_long("Enter the credit card number:");
    if (checksum(n)==1)
    {
        //Evaluating card type as per conditions
       if ((n/100000000000000)==51 || (n/100000000000000)==52 || (n/100000000000000)==53 || (n/100000000000000)==54 || (n/100000000000000)==55)
       {
           printf("MASTERCARD\n");
       }
       else if ((n/10000000000000)==34 || (n/10000000000000)==37)
       {
           printf("AMEX\n");
       }
       else if ((n/1000000000000)==4)
       {
           printf("VISA\n");
       }
       else if ((n/1000000000000000)==4)
       {
           printf("VISA\n");
       }
       else
       {
           printf("INVALID\n");
       }
    }
    else
    {
        printf("INVALID\n");
    }
}