#include <iostream>
#include <string.h>

using namespace std;

int main() {
  string str1 = "GACCATACTGATA";
  string str2 = "GACCATACTGACA";

  // Iterate over each character in the first string.
  for (int i = 0; i < str1.length(); i++) 
  {
    // Compare the current character to the corresponding character in the second string.
    if (str1[i] == str2[i]) 
    {
      // If the characters are not equal, print a message.
      cout << "The characters at index " << i << " are equal." << endl;
    }
    else if (str1[i] != str2[i])
    cout<<"The characters at index "<< i << " are not equal." << endl;
  }

  return 0;
}