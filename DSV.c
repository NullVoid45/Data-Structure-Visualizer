#include <stdio.h>
#define MAX 10

int s[MAX], top = -1, n = MAX;

__declspec(dllexport) int push(int val) {
    if (top == n - 1) {
        return -1;
    } else {
        top++;
        s[top] = val;
        return 0;
    }
}

__declspec(dllexport) int pop() {
    if (top == -1) {
        return -1;
    } else {
        int val = s[top];
        top--;
        return val;
    }
}

__declspec(dllexport) int* get_stack(int *size) {
    *size = top + 1;
    return s;
}