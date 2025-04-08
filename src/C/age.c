#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main()
{
    int n,num=0,count=0,k=0,j=0;
    scanf("%d",&n);
    char s[100][100];
    for(int i=0;i<n;i++)
    {
        fgets(s[i],100,stdin);
        s[i][strcspn(s[i],"\n")] = '\0';
    }
    char age[3];
    for(int i=0;i<n;i++)
    {
            strncpy(age,s[i]+11,2);
            age[2] = '\0';
            num = atoi(age);
            if(num > 60)
            {
                printf("%d\n",num);
                count++;
            }

    }
    printf("%d",count);

}