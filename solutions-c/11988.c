#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct {
    char letter;
    Node next;
    Node prev;
}
Node;

int main(void) {
    // char *str = malloc(100);
    // scanf("%s", str);
    // free(s)
    char str[100];
    
    Node answer[100];

    // get the input string
    scanf("%s", str);

    // loop over the input
    for (int i = 0; i < strlen(str); i++) {
        if (i == 0) {
            answer[i].letter = str[i];
            answer[i].next = NULL;
            answer[i].prev = NULL;
        } else if (strcmp(str[i], "[") == 0) {
            // go to node 0
            // add node
        } else if (strcmp(str[i], "]") == 0) {
            // go to last node
            // add node
        }
    }
}

// add node



// char *s = malloc(100)
// scanf("%", s);








// free(s)