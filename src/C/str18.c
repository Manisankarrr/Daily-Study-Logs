#include<stdio.h>
#include<string.h>
#include<ctype.h>

int main(){
    char s[100];
    printf("Enter a string: ");
    fgets(s, 100, stdin);
    s[strcspn(s, "\n")] = '\0';
    int n = strlen(s),count=0;
    for(int i =0 ; i < n ; i++){
        count = 1;
        while( 1 < n-1 && s[i] == s[i+1]){
            count++;
            i++;
        }
        if(count>1){
            printf("%c => %d\n",s[i], count);
        }

    }
}