//
// Created by 정지용 on 2021/09/27.
//

#include <stdio.h>
#include <stdlib.h>

typedef int element;
typedef struct stackNode {
    element data;
    struct stackNode *link;
} stackNode;

typedef struct {
    stackNode *top;
} linkedStackType;

void init(linkedStackType *s) {
    s->top = NULL;
}

int is_empty(linkedStackType *s) {
    return (s->top == NULL);
}

void push_back(linkedStackType *s, element item) {
    stackNode *temp = (stackNode *)malloc(sizeof(stackNode));
    temp->data = item;
    temp->link = s->top;
    s->top = temp;
}

void print_result(linkedStackType *s) {
    for (stackNode *p = s->top; p != NULL; p = p->link)
        printf("%c\n", p->data);
}

element pop(linkedStackType *s) {
    if (is_empty(s)) {
        fprintf(stderr, "스택이 비어있음.\n");
        exit(1);
    } else {
        stackNode *temp = s->top;
        element data = temp->data;
        s->top = s->top->link;
        free(temp);
        return data;
    }
}

element peek(linkedStackType *s) {
    if (is_empty(s)) {
        fprintf(stderr, "스택이 비어있음. \n");
        exit(1);
    } else {
        return s->top->data;
    }
}

int main() {
    int size;
    linkedStackType* seq = NULL;
    linkedStackType* sigma = NULL;
    linkedStackType* result = NULL;
    linkedStackType* result2 = NULL;
    int *input = NULL;

    scanf("%d", &size);
    input = (int*) malloc(sizeof(int) * size);

    result = (linkedStackType*) malloc(sizeof(linkedStackType));
    result2 = (linkedStackType*) malloc(sizeof(linkedStackType));
    seq = (linkedStackType*) malloc(sizeof(linkedStackType));
    sigma = (linkedStackType*) malloc(sizeof(linkedStackType));

    if (seq == NULL || input == NULL || sigma == NULL) {
        fprintf(stderr, "Memory allocation failure\n");
        exit(1);
    }

    init(result);
    init(result2);
    init(seq);
    init(sigma);

    for (int i = 0; i < size; i++) {
        scanf("%d", &input[i]);
    }
    for (int i = 0; i < size; i++) {
        push_back(sigma, size - i);
    }
    peek(sigma);

    for (int i = 0; i < size; i++) {
        while (!is_empty(sigma)) {
            if (input[i] >= peek(sigma)) {
                push_back(seq, pop(sigma));
                push_back(result, '+');
            }
            else
                break;
        }
        if (peek(seq) > input[i]) {
            printf("NO");
            exit(1);
        } else {
            push_back(result, '-');
        }
    }

    while (!is_empty(result))
        push_back(result2, pop(result));

    print_result(result2);

    return 0;
}