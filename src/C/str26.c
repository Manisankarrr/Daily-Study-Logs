#include <stdio.h>
#include <string.h>

int main() {
    char s[100], r[100];

    printf("Enter the main string: ");
    fgets(s, sizeof(s), stdin);
    s[strcspn(s, "\n")] = '\0';  // Remove newline

    printf("Enter the substring to find: ");
    fgets(r, sizeof(r), stdin);
    r[strcspn(r, "\n")] = '\0';  // Remove newline

    char *found = strstr(s, r);
    if (found != NULL) {
        int index = found - s;
        printf("Substring '%s' found at index: %d\n", r, index);
    } else {
        printf("Substring '%s' not found\n", r);
    }

    return 0;
}
