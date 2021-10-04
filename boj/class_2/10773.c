//
// Created by 정지용 on 2021/10/04.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define true	1
#define false	0

#define LIST_LEN	100000
typedef int element;

typedef struct __ArrayList
{
    element arr[LIST_LEN];
    int __front;
} ArrayList;

typedef ArrayList List;

void init(List* list) {
    list->__front = 0;
}

void push(List* list, element item) {
    if (list->__front < LIST_LEN) {
        list->arr[list->__front++] = item;
    } else exit(0);
}

int empty(List* list) {
    if (!list->__front) {
        return true;
    } else return false;
}

element pop(List* list) {
    if(!empty(list)) {
        return list->arr[--list->__front];
    } else return -1;
}

int size(List* list) {
    return list->__front;
}

element top(List* list) {
    if(!empty(list)) {
        return list->arr[list->__front - 1];
    } else return -1;
}

int main() {
    int N, tmp, res = 0;
    List money;

    init(&money);
    scanf("%d", &N);

    for (int i = 0; i < N; i++) {
        scanf("%d", &tmp);
        if (tmp == 0) {
            pop(&money);
        } else {
            push(&money, tmp);
        }
    }

    while (!empty(&money)) {
        res += pop(&money);
    }

    printf("%d", res);
}