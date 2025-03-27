//Find the maximum of a character in a given string .Igore the case(lower or upper case).Return
 //the character in lower case Input:Test Output:t
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main() {
    char str[100];
    fgets(str, 100, stdin);
    str[strcspn(str, "\n")] = '\0';
    int max = 0,count=1,n=strlen(str);
    char maxChar;

    for (int i = 0; i<n; i++) {
        count = 1;
        if(str[i]!='\0'){
        for(int j = i+1; j<n;j++)
        {
            if (tolower(str[i]) == tolower(str[j])) {
                count++;
                str[j]='\0';
            }
        }
        if (count > max) {
            max = count;
            maxChar = str[i];
        }
    }
    }

    printf("Maximum character in lower case: %c\n", tolower(maxChar));

    return 0;
}
#