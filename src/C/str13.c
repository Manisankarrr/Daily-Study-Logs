#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    char s[100],r[100];
    printf("Enter a string: ");
    fgets(s, 100, stdin);
    s[strcspn(s, "\n")] = '\0'; // Remove trailing newline
    int n = strlen(s), count,k=0;

    for (int i = 0; i < n; i++) {
        count = 1;
        if (s[i] != '\0') {
            char current = tolower(s[i]); // Lowercase the current character
            for (int j = i + 1; j < n; j++) {
                if (current == tolower(s[j])) { // Check for duplicates
                    count++;
                    s[j] = '\0'; // Mark as processed
                }
            }
            if(count == 1) {
                printf("%c",current); // Add unique character to reversed string
            }
            
        }
    }

    return 0;
}