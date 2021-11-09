#include "helpers.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i=0;i<height;i++)
    {
        for (int j=0;j<width;j++)
        {
            float g;
            g=image[i][j].rgbtRed+image[i][j].rgbtGreen+image[i][j].rgbtBlue;
            g=g/3;
            //Rounding off
            int gg=g+0.5;
            BYTE G=gg;
            //MOdifying
            image[i][j].rgbtRed=G;
            image[i][j].rgbtGreen=G;
            image[i][j].rgbtBlue=G;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i=0;i<height;i++)
    {
        for (int j=0;j<width;j++)
        {
            float sepiaRed,sepiaGreen,sepiaBlue;
            sepiaRed = .393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue;
            sepiaGreen = .349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue;
            sepiaBlue = .272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue;
            //Rounding off
            int sr=(sepiaRed+0.5);
            int sg=(sepiaGreen+0.5);
            int sb=(sepiaBlue+0.5);
            //applying cap at 255
            if (sr>255)
            {
                sr=255;
            }
            if (sg>255)
            {
                sg=255;
            }
            if (sb>255)
            {
                sb=255;
            }
            BYTE R=sr;
            BYTE G=sg;
            BYTE B=sb;
            //modifying
            image[i][j].rgbtRed=R;
            image[i][j].rgbtGreen=G;
            image[i][j].rgbtBlue=B;
        }
    }
    
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    //for even number of pixels.. all pixels swapped
    if ((width%2)==0)
    {
        for (int i=0; i<height;i++)
        {
            for (int j=0, h=(width-1);j<width/2;j++,h--)
            {
                //swapping and modifying
                BYTE tempr='\0';
                BYTE tempg='\0';
                BYTE tempb='\0';
                tempr=image[i][j].rgbtRed;
                tempg=image[i][j].rgbtGreen;
                tempb=image[i][j].rgbtBlue;
                image[i][j].rgbtRed=image[i][h].rgbtRed;
                image[i][j].rgbtGreen=image[i][h].rgbtGreen;
                image[i][j].rgbtBlue=image[i][h].rgbtBlue;
                image[i][h].rgbtRed=tempr;
                image[i][h].rgbtGreen=tempg;
                image[i][h].rgbtBlue=tempb;

            }
        }
    }
    else
    {
        //for odd number of pixels.. other than the middle column all pixels are to be swapped
        for (int i=0; i<height;i++)
        {
            for (int j=0, h=(width-1);j<((width-1)/2);j++,h--)
            {
                //swapping and modifying
                BYTE tempr='\0';
                BYTE tempg='\0';
                BYTE tempb='\0';
                tempr=image[i][j].rgbtRed;
                tempg=image[i][j].rgbtGreen;
                tempb=image[i][j].rgbtBlue;
                image[i][j].rgbtRed=image[i][h].rgbtRed;
                image[i][j].rgbtGreen=image[i][h].rgbtGreen;
                image[i][j].rgbtBlue=image[i][h].rgbtBlue;
                image[i][h].rgbtRed=tempr;
                image[i][h].rgbtGreen=tempg;
                image[i][h].rgbtBlue=tempb;
            }
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    
    return;
}
