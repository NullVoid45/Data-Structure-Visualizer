#include <stdio.h>
#define MAX 10

int s[MAX], top = -1, n = MAX;

__declspec(dllexport) void push(int val) {
    if (top == n - 1) {
        printf("Stack overflow\n");
    } else {
        top++;
        s[top] = val;
        printf("Value %d inserted\n", val);
    }
}

__declspec(dllexport) int pop() {
    if (top == -1) {
        printf("Underflow\n");
        return -1;
    } else {
        int val = s[top];
        top--;
        printf("Value %d deleted\n", val);
        return val;
    }
}

__declspec(dllexport) int* get_stack(int *size) {
    *size = top + 1;
    return s;
}
