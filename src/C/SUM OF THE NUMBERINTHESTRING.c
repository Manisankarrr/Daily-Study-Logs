#include <stdio.h>
#include <ctype.h>

int main() {
    char s[1000];
    fgets(s, sizeof(s), stdin);

    int sum = 0, cur = 0;

    for(int i=0;s[i] != '\0';i++)
    {
        if(isdigit(s[i]))
        {cur = cur * 10 + (s[i] - '0');}
        else{
            sum += cur;
            cur =0;
        }
    }
    sum += cur;
    printf("%d\n", sum);
    return 0;
}

