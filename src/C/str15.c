//Isomorphic string
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(){
    char s1[100],s2[100];
    fgets(s1, 100, stdin);
    fgets(s2, 100, stdin);
    s1[strcspn(s1, "\n")] = '\0';
    s2[strcspn(s2, "\n")] = '\0';
    int n1 = strlen(s1);
    int n2 = strlen(s2);
    if(n1!=n2)
    return 0;
    int map1[26] = {0}, map2[26] = {0};
    for(int i=0; i<n1; i++){
        s1[i] = tolower(s1[i]);
        s2[i] = tolower(s2[i]);
        if(map1[s1[i]-'a']!=map2[s2[i]-'a'])
        {
            "Not isomorphic\n";
            return 0;
        }
    }
    printf("Isomorphic\n");
}