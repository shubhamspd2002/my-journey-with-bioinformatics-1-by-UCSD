#include<iostream>
#include<string.h>
using namespace std;
int main ()
{
    char text[500] = "GACCATACTGATA";
    char pattern[10] = "ATA";
    char text_copy[50];
    int i, k, count = 0;
    i = strlen(text); //
    k = strlen(pattern); 
    for (int l = 0; l<(i-k); l++)
    {
        strncpy(text_copy, text,  ); //here after the comma, you have to input the number of chars that should transfer from text to text_copy. note that every time the 1st alphabet from the text should be removed to move forward 

        for (int m = 0; m<k; m++)
        {
            if(text_copy[m] ==  pattern[m])
            {
                count += 1;
            }
        }
        for (int j = 0; j>k; j++)
        {
            text.erase(text.begin());
        }
    }
    cout<<count;
    return 0;
}
