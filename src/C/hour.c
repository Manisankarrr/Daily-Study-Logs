#include<stdio.h>
#include<string.h>
int main(){
    char time[9];
    int h, m, s;
    scanf("%8s", time);
    sscanf(time, "%d:%d:%d",&h,&m,&s);
    if((h>=0 && h<=23) && (m>=0 && m<=59) && (s>=0 && s<=59))
    {
        printf("%s",time);
    }
    else
    {
        printf("Invalid time");
    }
    return 0;

}