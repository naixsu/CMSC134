int main() {
    __asm__("xor %eax, %eax;"
            "inc %eax;"
            "mov %ebx, %eax;"
            "leave;"
            "ret;"
    );
}