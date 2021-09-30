//
// Created by 정지용 on 2021/09/30.
//
// 조건이 길이, 사전순ㅇ이 아니라 그냥 사전순이기만 해서 그럼

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int n;
char **predicate;

void merge(char **arr, int p, int q, int r) {
    int i = p, j = q + 1, k = p;
    char nullStr[] = "0";
    while (i <= q && j <= r) {
        if (strlen(arr[i]) < strlen(arr[j])) {
            strcpy(predicate[k++], arr[i++]);
        } else if (strlen(arr[i]) == strlen(arr[j])) {
            if (strcmp(arr[i], arr[j]) == 0) strcpy(arr[j], nullStr);
            if (strcmp(arr[i], arr[j]) < 0) {
                strcpy(predicate[k++], arr[i++]);
            } else strcpy(predicate[k++], arr[j++]);
        } else strcpy(predicate[k++], arr[j++]);
    }
    while (i <= q) strcpy(predicate[k++], arr[i++]);
    while (j <= r) strcpy(predicate[k++], arr[j++]);
    for (int l = p; l <= r; l++) strcpy(arr[l], predicate[l]);
}
void sort(char **arr, int p, int r) {
    int q;
    if (p < r) {
        q = (p + r) / 2;
        sort(arr, p, q);
        sort(arr, q + 1, r);
        merge(arr, p, q, r);
    }
}

int main() {
    char nullStr[] = "0";
    scanf("%d", &n);

    char **words = (char **) malloc(sizeof(char *) * n);
    predicate = (char **) malloc(sizeof(char *) * n);
    for (int i = 0; i < n; i++) {
        predicate[i] = (char *) malloc(sizeof(char) * 51);
        words[i] = (char *) malloc(sizeof(char) * 51);
        scanf("%s", words[i]);
    }

    sort(words, 0, n - 1);
    for (int i = 0; i < n; i++) {
        if (!strcmp(words[i], nullStr)) continue;
        printf("%s\n", words[i]);
    }
}