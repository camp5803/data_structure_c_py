//
// Created by 정지용 on 2021/09/28.
//

#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, k, count = 0, t;
    int* m;
    scanf("%d %d", &n, &k);

    m = (int*) malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++) scanf("%d", &m[i]);
    n--;
    while (k) {
        if (k >= m[n]) {
            t = k / m[n];
            count += t;
            k -= m[n] * t;
            if (!k) break;
        }

        if (k < m[n] && k > m[n-1]) {
            t = k / m[n-1];
            count += t;
            k -= m[n-1] * t;
        }
        n--;
    }
    printf("%d", count);
}