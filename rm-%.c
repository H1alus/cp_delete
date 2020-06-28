#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define NAME_LENGTH 10000

int main (int argc, char *argv[]) {
    char *name = (char *) malloc(NAME_LENGTH);
#ifdef ARG
    strcpy(name, argv[1]);
#endif
#ifndef ARG
    fgets(name, NAME_LENGTH, stdin);
#endif
    char value[3];
    int int_v;

    for (int i = 0; i < strlen(name); i++) {
        if (name[i] == '%') {
            value[0] = name[i + 1];
            value[1] = name[i + 2];
            value[2] = '\0';
            int_v = (int) strtol(value, NULL, 16);
            printf("%c", int_v);
            i = i + 2;
        }
        else if(name[i] != '%')  {
            printf("%c", name[i]);
        }
    }
    free(name);
}