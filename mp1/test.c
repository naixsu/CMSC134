#include <stdio.h>
#include <stdlib.h>

void vuln() {
    char buffer[8];
    gets(buffer);
}

int main() {
    vuln();
    exit(1);
}