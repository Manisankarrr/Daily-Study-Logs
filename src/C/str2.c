#include<stdio.h>
#include<string.h>
int main()
{
    int n;
    scanf("%d",&n);
    printf("Enter a string: ");
    while(getchar() != '\n');
    char s[100][100];
    for(int i=0; i<n; i++)
    {
        fgets(s[i],100,stdin);
        s[i][strcspn(s[i],"\n")] = '\0';
    }
    for(int i=0;i<n;i+=2)
    {
        printf("%s\n",s[i]);
    }
    
}