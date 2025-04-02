#include <stdio.h>
#include <string.h>
int main() {
    int n;
    char s[100][100];
    scanf("%d",&n);
    
    getchar()!= '\n';
    int first=0,second=0;

    for(int i=0;i<n; i++)
    {
        fgets(s[i],100,stdin);
        s[i][strcspn(s[i],"\n")] = '\0';
    }

    for(int i=0;i<n; i++)
    {
        int len = strlen(s[i]);
        if(len > first)
        {
            second = first;
            first = len;
        }
        else if(len > second && len < first)
        {
            second = len;
        }
    }

    if(second==0){
        printf("No second longest string found.\n");
        return 0;
    }
printf("Second longest string: %d\n",second);

}