//RETURN NUMBER OF PEOPLE WHOSE AGE ABOVE 60
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int main()
{
    int n,count=0,j=0,num;
    scanf("%d",&n);
    while(getchar()!='\n');
    char s[100][100];
    for(int i=0;i<n;i++)
    {
        fgets(s[i],100,stdin);
        s[i][strcspn(s[i],"\n")] = '\0';
    }
    char age[3];
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<2;j++)
        {
            age[j] = s[i][11+j];
        }    
        age[j]!= '\0';
        j=0,num=0;
        while(age[j]!='\0')
        {
            num = (num*10) + (age[j]-'0');
            j++;
        }
        printf("%d\n",num);
        if(num>60)
        {
            count++;
        }
    }
    printf("%d",count);
}