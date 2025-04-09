#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    char s[100], r[100], s1[100], r1[100];
    fgets(s, 100, stdin);
    s[strcspn(s, "\n")] = '\0';
    fgets(r, 100, stdin);
    r[strcspn(r, "\n")] = '\0';

    strcpy(s1, s);
    strcpy(r1, r);

    char *token1 = strtok(s, ".");
    int one1 = atoi(token1);
    token1 = strtok(NULL, ".");
    int two1 = atoi(token1);
    token1 = strtok(NULL, ".");
    int thr1 = atoi(token1);

    char *token2 = strtok(r, ".");
    int one2 = atoi(token2);
    token2 = strtok(NULL, ".");
    int two2 = atoi(token2);
    token2 = strtok(NULL, ".");
    int thr2 = atoi(token2);

    if (one1 > one2) {
        printf("%s is greater", s1);
    } else if (one1 < one2) {
        printf("%s is greater", r1);
    } else { // one1 == one2
        if (two1 > two2) {
            printf("%s is greater", s1);
        } else if (two1 < two2) {
            printf("%s is greater", r1);
        } else { // two1 == two2
            if (thr1 > thr2) {
                printf("%s is greater", s1);
            } else if (thr1 < thr2) {
                printf("%s is greater", r1);
            } else { // thr1 == thr2
                printf("%s & %s are equal", s1, r1);
            }
        }
    }

    return 0;
}