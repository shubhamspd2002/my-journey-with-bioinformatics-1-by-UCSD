#include<iostream>
#include<string.h>
using namespace std;
int main ()
{
    char genome[1000] = "TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT";
    int count = 0;
    int minima;

    cout<<count<<" ";
    
    for (int i=0; i<strlen(genome); i++)
    {
        if(genome[i] == 'C')
        {
            count--;
            cout<<count<<" ";
        }

        else if(genome[i] == 'G')
        {
            count++;
            cout<<count<<" ";
        }

        else 
        cout<<count<<" ";

    }
    return 0;
}