#include <string>
#include <iostream>
using namespace std;

bool isPolindrome(string input)
{
    int i = 0;
    int j = input.length() - 1;
    while( i < j )
    {
        if(input[i] != input[j])
            return false;
        i++;
        j--;
    }
    return true;
}

int main()
{
    std::cout << isPolindrome("racecar") << std::endl;
    std::cout << isPolindrome("abcdef") << std::endl;

    return 0;
}