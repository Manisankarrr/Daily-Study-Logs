#include<stdio.h>
#include<string.h>
#include<ctype.h>

int main(){
    char s[100], t[100];
    printf("Enter a string: ");
    fgets(s, 100, stdin);
    s[strcspn(s, "\n")] = '\0';
    int n = strlen(s), count=0;
    fgets(t, 100, stdin);
    t[strcspn(t, "\n")] = '\0';
    int m = strlen(t);
    if (n != m)
    {
        printf("Not Anagram\n");
        return 0;
    }
    int fre1[26] = {0};
    for (int i = 0; i < n; i++)
    {
        s[i] = tolower(s[i]);
        t[i] = tolower(t[i]);
        fre1[s[i]-'a']++; 
    }
    for(int i = 0; i < n; i++)
    {
        fre1[t[i]-'a']--;
    }
    for(int i=0;i<n;i++)
    {
        if(fre1[i]!=0)
        {
            printf("not Anagram");
            return 0;
        }
    }
    printf("\n Anagram");

}