//
// Created by 정지용 on 2021/09/29.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define true	1
#define false	0

#define LIST_LEN	10000
typedef int element;

typedef struct __ArrayList
{
    element arr[LIST_LEN];
    int __front;
    int curPosition;
} ArrayList;

typedef ArrayList List;

void init(List* list) {
    list->__front = 0;
    list->curPosition = 0;
}

void push(List* list, element item) {
    if (list->__front < LIST_LEN) {
        list->arr[list->__front++] = item;
    } else exit(0);
}

int empty(List* list) {
    if (list->curPosition == list->__front || !list->__front) {
        return true;
    } else return false;
}

element pop(List* list) {
    if(!empty(list)) {
        return list->arr[++list->curPosition - 1];
    } else return -1;
}

int size(List* list) {
    return list->__front - list->curPosition;
}

element front(List* list) {
    if(!empty(list)) {
        return list->arr[list->curPosition];
    } else return -1;
}

element back(List* list) {
    if(!empty(list)) {
        return list->arr[list->__front - 1];
    } else return -1;
}

int main() {
    int a;
    char b[100];
    int c;
    List list;
    init(&list);

    scanf("%d", &a);
    for(int i = 0; i < a; i++) {
        scanf("%s", b);
        if(!strcmp(b, "push")) {
            scanf("%d", &c);
            push(&list, c);
        }
        else if(!strcmp(b, "pop")) { printf("%d\n", pop(&list)); }
        else if(!strcmp(b, "size")) { printf("%d\n", size(&list));}
        else if(!strcmp(b, "empty")) { printf("%d\n", empty(&list)); }
        else if(!strcmp(b, "back")) { printf("%d\n", back(&list)); }
        else if(!strcmp(b, "front")) { printf("%d\n", front(&list)); }
    }
}