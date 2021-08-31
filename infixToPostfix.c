//
// Created by 정지용 on 2021/09/01.
//
#define MAX_SIZE 50

#include <stdio.h>
#include <string.h>
#include "nodeStack.c"

int main() {
    char expression[MAX_SIZE];
    char converted[MAX_SIZE] = {0, };
    int count = 0;
    linkedStackType *stack = (linkedStackType*)malloc(sizeof(linkedStackType));

    init(stack);

    printf("[<] 수식 입력: ");
    scanf("%s", expression);

    for (int i = 0; i < strlen(expression); i++) {
        switch (expression[i]) {
            case '+':
                if (is_empty(stack)) {
                    push_back(stack, '+');
                } else if (peek(stack) == '-' || peek(stack) == '+') {
                    converted[count++] = pop(stack);
                    push_back(stack, '+');
                } else {
                    while (!is_empty(stack)) {
                        converted[count++] = pop(stack);
                    }
                    push_back(stack, '+');
                }
                break;
            case '-':
                if (is_empty(stack)) {
                    push_back(stack, '-');
                } else if (peek(stack) == '-' || peek(stack) == '+') {
                    converted[count++] = pop(stack);
                    push_back(stack, '-');
                } else {
                    while (!is_empty(stack)) {
                        converted[count++] = pop(stack);
                    }
                    push_back(stack, '-');
                }
                break;
            case '*':
                if (is_empty(stack)) {
                    push_back(stack, '*');
                } else if (peek(stack) == '/' || peek(stack) == '*') {
                    while (!is_empty(stack)) {
                        converted[count++] = pop(stack);
                    }
                    push_back(stack, '*');
                } else {
                    push_back(stack, '*');
                }
                break;
            case '/':
                if (is_empty(stack)) {
                    push_back(stack, '/');
                } else if (peek(stack) == '/' || peek(stack) == '*') {
                    while (!is_empty(stack)) {
                        converted[count++] = pop(stack);
                    }
                    push_back(stack, '/');
                } else {
                    push_back(stack, '/');
                }
                break;
            default:
                converted[count++] = expression[i];
                break;
        }
    }
    while (!is_empty(stack)) { converted[count++] = pop(stack); };
    printf("[>] Converted expression: %s\n", converted);
}