
#include <stdio.h>
#include <string.h>

int main() {
    char s[100];
    fgets(s,100,stdin);
    s[strcspn(s,"\n")] = '\0';
    int sum =0;
    for(int i=0;s[i]!='\0';i++)
    {
        if(s[i]==s[i+1])
        {
            printf("2");
            sum += 2;
            i++;
        }
        else
        {
            printf("1");
            sum +=1;
        }
    }
    printf("\n%d",sum*sum);

    return 0;
}