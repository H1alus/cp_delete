#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main (int argc, char *argv[]) {  
    char value[2];
    char c;
    for (int i = 0; i < strlen(argv[1]); i++) {
        if (argv[1][i] == '%') {
            value[0] = argv[1][i + 1];
            value[1] = argv[1][i + 2];
            long int int_v = strtol(value, NULL, 16);
            printf("%c", int_v);
            i = i + 2;
        } else {
            printf("%c", argv[1][i]);
        }
    }
}
