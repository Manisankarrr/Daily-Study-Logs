#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>
int main() {
    char s[100],r[100];
    printf("Enter a string: ");
    fgets(s, 100, stdin);
    s[strcspn(s, "\n")] = '\0';
    int n = strlen(s)-1, count=0,start=0,end=strlen(s)-1,k=0,max=0,min=100;
    char *token = strtok(s," ");
    while(token != NULL)
    {
        int len = strlen(token);
        if(len>max)
        {
            max = len;
        }
        if(len<min)
        {
            min = len;
        }
        token = strtok(NULL, " ");
    }
    
    printf("Max word length: %d\n", max);
    printf("Min word length: %d\n", min);

    // while(n>=0){

    //     if(s[n]==' ')
    //     {
    //         count = 0;
    //         start = n+1;
    //         for(int i=start;i<=end;i++)
    //         {
    //             r[k++] = s[i];
    //             count++;
    //         }
    //         end = n-1;
    //         r[k++] =' ';
    //         if(count>max)
    //         {
    //             max = count;
    //         }
    //         if(count<min)
    //         {
    //             min = count;
    //         }
    //     }
    //     n--;
    // }
    // count = 0;
    // for(int i=0;i<=end;i++)
    // {
    //     count++;
    //     r[k++] = s[i];
    // }
    // r[k] = '\0';
    // printf("Reversed string: %s\n", r);
    // if(count>max)
    // {
    //     max = count;
    // }
    // if(count<min)
    // {
    //     min = count;
    // }
}