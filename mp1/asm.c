int main() {
    __asm__("xor %eax, %eax;"
            "inc %eax;"
            "mov %eax, %ebx;"
            "leave;"
            "ret;"
    );
}