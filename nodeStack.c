#include <stdio.h> // nodeStack.c
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

int is_full(linkedStackType *s) {
    return 0;
}

void push_back(linkedStackType *s, element item) {
    stackNode *temp = (stackNode *)malloc(sizeof(stackNode));
    temp->data = item;
    temp->link = s->top;
    s->top = temp;
}

void print_stack(linkedStackType *s) {
    for (stackNode *p = s->top; p != NULL; p = p->link)
        printf("%d->", p->data);
    printf("NULL \n");
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