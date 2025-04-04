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
        printf("Not Isomorphic\n");
        return 0;
    }
    int fre1[26] = {0}, fre2[26] = {0};
    for (int i = 0; i < n; i++)
    {
        s[i] = tolower(s[i]);
        t[i] = tolower(t[i]);
        if(fre1[s[i]-'a']++ != fre2[t[i]-'a']++)
        {
            printf("Not Isomorphic");
        }
    }
    printf("\n Isomorphic");

}