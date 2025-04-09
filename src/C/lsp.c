#include <stdio.h>
#include <string.h>

int main() {
    char s[100], longest[100];
    fgets(s, sizeof(s), stdin);
    s[strcspn(s, "\n")] = '\0';  // remove newline

    int maxLen = 0;
    int start, end;
    int n = strlen(s);

    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            int left = i, right = j;
            int isPalindrome = 1;
            while (left < right) {
                if (s[left] != s[right]) {
                    isPalindrome = 0;
                    break;
                }
                left++;
                right--;
            }
            if (isPalindrome && (j - i + 1 > maxLen)) {
                maxLen = j - i + 1;
                start = i;
                end = j;
            }
        }
    }
    int k = 0;
    for (int i = start; i <= end; i++)
        longest[k++] = s[i];
    longest[k] = '\0';

    printf("Longest Palindromic Substring: %s\n", longest);
    return 0;
}
