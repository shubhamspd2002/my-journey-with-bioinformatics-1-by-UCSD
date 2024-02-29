#include <iostream>
#include<string.h>
using namespace std;
int main ()
{
    char A[10000] = "CTAGAAAGAATTACGGTACCCATCGATCTTGCTGTACAACGAGGCTATCGGACTCGAGTAAAAATGTGTTGCTCACGCATGCATCCCTCG";
/*the data entered in char A is from 5' to 3'. the complementary nucleotide would be 3' to 5' but we want output of the complementary strand 
as 5' to 3'. like for eg: if input strand is AAAACCCGGT then output will be ACCGGGTTTT*/

    for(int i=strlen(A)-1; i>=0; i--)
    {
        if (A[i] == 'A')
        cout<<"T";
        else if (A[i] == 'T')
        cout<<"A";
        else if (A[i] == 'G')
        cout<<"C";
        else if (A[i] == 'C')
        cout<<"G";
    }

    

}