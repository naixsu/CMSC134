// vuln.c
#include <stdio.h>

void vuln() {
    char buffer[8];
    gets(buffer);
    printf("%s", buffer);
}

int main() {
    vuln();
}