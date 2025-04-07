#include<stdio.h>
#include<string.h>

int main() {
    char s[100],r[100];
    printf("Enter a string: ");
    fgets(s, 100, stdin);
    s[strcspn(s, "\n")] = '\0'; // Remove trailing newline
    int n = strlen(s), count,k=0;
    int freq[26] = {0}; // Frequency array for lowercase letters

    for(int i = 0;s[i]!='\0';i++)
    {
        if(s[i] >= 'a' && s[i] <= 'z')
        {
            freq[s[i]-'a']++;
        }
    }
    for(int i=0;i<26;i++)
    {
        if(freq[i]==0)
        {
            printf("Not pangram");
            return 0;
        }
    }
    printf("pangram");
    
    return 0;
}