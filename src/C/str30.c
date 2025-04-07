#include<stdio.h>
#include<string.h>

int main()
{
    char s1[9];
    int h, m, s;
    scanf("%8s",s1);
    sscanf(s1, "%d:%d:%d", &h, &m, &s);
    if((h>=0 && h<24) && (m>=0 && m<60) && (s>=0 && s<60))
    {
        printf("Valid time");
    }
    else
    {
        printf("Invalid\n");
    }

}