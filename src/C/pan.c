#include<stdio.h>
#include<string.h>
#include<ctype.h>

int main()
{
    char s[100],r[100];
    printf("Enter a string: ");
    fgets(s, sizeof(s), stdin); // Read a line of input
    s[strcspn(s,"\n")] = '\0'; // Remove the newline character if present
    fgets(r, sizeof(r), stdin); // Read a line of input
    r[strcspn(r,"\n")] = '\0'; // Remove the newline character if present
    int i = 0, j = 0, n1 = strlen(s),sum=0,res = 0,k=0;
    int freq1[26] ={0};
    int freq2[26] = {0};
    int n2 = strlen(r);
    if(n1!=n2)
    {
        printf("Not anagram\n");
        return 0;
    }
    for(int i=0;i<n1;i++)
    {
        s[i] = tolower(s[i]);
        r[i] = tolower(r[i]);
        if(freq1[s[i]-'a']++ != freq2[r[i]-'a']++)
        {
            printf("Not Isomorphic");
            return 0;
        }
    }
    printf("Isomorphic");

    // for(int i=0;i<n1;i++)
    // {
    //     s[i] = tolower(s[i]);
    //     freq1[s[i]-'a']++;
    // }
    // for(int i=0;i<n2;i++)
    // {
    //     r[i] = tolower(r[i]);
    //     freq1[r[i]-'a']--;
    // }
    // for(int i = 0;i<26;i++)
    // {
    //     if(freq1[i] != 0)
    //     {
    //         printf("Not anagram\n");
    //         return 0;
    //     }
    // }
    // printf("Anagram\n");



    // for(int i=0;i<n;i++)
    // {
    //     s[i] = tolower(s[i]);
    //     freq[s[i]-'a']++;
    // }
    // for(int i=0;i<26;i++)
    // {
    //     if(freq[i]==0)
    //     {
    //         printf("Not pangram");
    //         return 0;
    //     }
    // }
    // printf("Pangram\n");
    return 0;
}