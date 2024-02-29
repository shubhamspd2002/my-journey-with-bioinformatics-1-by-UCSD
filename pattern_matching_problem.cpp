#include<iostream>
#include<cstring>
using namespace std;
int main ()
{
    int count = 0;
    char pattern[100] = "ATA";
    char genome[10000] = "ATAGCATACGATTATATAGC";
    
    for(int i=0; i<strlen(genome); i++)
    {

    if(pattern[0] == genome[i])

    {
        
        for (int j=0; j<strlen(pattern); j++)       //this for loop is used first cause according to length of the pattern we have to run the loop till then.

        {
            
            int k = i;
              

                if((j-i==k) && (pattern[j] == genome[k]))

                    {
                        count += 1;
                
                    }

            

            
        }

        if(count == strlen(pattern))
        {
            cout<<i<<" ";
        }

    }


    }
return 0;
}