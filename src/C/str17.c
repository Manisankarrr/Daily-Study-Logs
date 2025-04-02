#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>

int main() {
    char s[100];
    printf("Enter a string: ");
    fgets(s, 100, stdin);
    s[strcspn(s, "\n")] = '\0';
    int count = 0,start=0,end=strlen(s)-1;
    char temp;
    while(start<end)
    {
        // Swap characters
        temp = s[start];
        s[start] = s[end];
        s[end] = temp;
        start++;
        end--;
    }
    printf("Reversed string: %s\n", s);
    for(int i=0; i<strlen(s); i++)
    {
        if(i % 2 != 0) printf("%c", s[i]);
    }
    
}
