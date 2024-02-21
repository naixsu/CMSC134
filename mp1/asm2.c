int vuln() {
    __asm__(
            "push %ebp;"
            "move %ebp, %esp;"
            "sub %esp, 8;"
            "lea %eax, [ebp - 8];"
            "push %eax;"
            "call gets;"

            "add %esp, 12;"
            "pop %ebp;"
            "ret;"

    );
}


int main() {
    __asm__(
            "call vuln;"
    );
}

int infinite_loop() {
    
}