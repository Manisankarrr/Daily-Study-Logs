#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    char s[100];
    printf("Enter a string: ");
    fgets(s, 100, stdin);
    s[strcspn(s, "\n")] = '\0'; // Remove trailing newline

    int sum = 0;
    int num = 0;
    int in_number = 0;

    for (int i = 0; s[i] != '\0'; i++) {
        if (isdigit(s[i])) {
            num = num * 10 + (s[i] - '0');
            in_number = 1;
        } else if (in_number==1) {
            sum += num;
            num = 0;
            in_number = 0;
        }
    }

    // If the string ends with a number
    if (in_number) {
        sum += num;
    }
    int len = strlen(sum);
    
    printf("Sum of numbers: %d\n", sum);
    return 0;
}
