//
// Created by 정지용 on 2021/10/04.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SIZE 10000
#define true    1
#define false   0

typedef int element;

typedef struct Node {
    element data;
    struct Node* next;
    struct Node* prev;
} node;

typedef struct {
    node* head;
    node* tail;
    int size;
} deque;

void init(deque* d) {
    d->head = NULL;
    d->tail = NULL;
    d->size = 0;
}

int empty(deque* d) {
    if (d->head == NULL) return 1;
    return 0;
}

void push_front(deque* d, element item) {
    node* newNode = (node *) malloc(sizeof(node));
    newNode->data = item;

    newNode->next = d->head;

    if (empty(d)) {
        d->tail = newNode;
    } else {
        d->head->prev = newNode;
    }

    newNode->prev = NULL;
    d->head = newNode;
    ++d->size;
}

void push_back(deque* d, element item) {
    node* newNode = (node *) malloc(sizeof(node));
    newNode->data = item;

    newNode->prev = d->tail;

    if (empty(d)) {
        d->head = newNode;
    } else {
        d->tail->next = newNode;
    }

    newNode->next = NULL;
    d->tail = newNode;
    ++d->size;
}

element pop_front(deque* d) {
    node* onode = d->head;
    element item;
    if(empty(d)) return -1;
    item = d->head->data;

    d->head = d->head->next;
    free(onode);

    if (d->head == NULL) d->tail = NULL;
    else d->head->prev = NULL;

    --d->size;

    return item;
}

element pop_back(deque* d) {
    node* onode = d->tail;
    element item;
    if(empty(d)) return -1;
    item = d->tail->data;

    d->tail = d->tail->prev;
    free(onode);

    if (d->tail == NULL) d->head = NULL;
    else d->tail->next = NULL;

    --d->size;

    return item;
}

element front(deque* d) {
    if(empty(d)) return -1;
    return d->head->data;
}

element back(deque* d) {
    if(empty(d)) return -1;
    return d->tail->data;
}

element size(deque* d) {
    return d->size;
}

int main() {
    int N, K, L;
    int location = 0, tmp, cnt, max;
    deque d;

    scanf("%d", &N);

    for (int i = 0; i < N; i++) {
        init(&d);
        max = 0;
        cnt = 0;
        tmp = 0;
        scanf("%d %d", &K, &location);


        for (int j = 0; j < K; j++) {
            scanf("%d", &L); // 사망시점
            push_back(&d, L);
        }

        while (true) {
            max = 0;
            for (int cex = 0; cex < size(&d); cex++) {
                if (front(&d) > max)
                    max = front(&d);
                push_back(&d, pop_front(&d));
            }

            while (front(&d) != max) {
                push_back(&d, pop_front(&d));
                if (location == 0) {
                    location = size(&d) - 1;
                } else location--;
            }
            if (front(&d) == max) {
                if (location == 0) {
                    while (!empty(&d)) {
                        pop_front(&d);
                    }
                    cnt++;
                    break;
                }
                pop_front(&d);
                location--;
                cnt++;
            }
        }
        printf("%d\n", cnt);
    }
}