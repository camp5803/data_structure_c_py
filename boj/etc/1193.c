//
// Created by 정지용 on 2021/09/28.
//

#include <stdio.h>

int sigma (int n) { return n ? n + sigma(n-1) : 0; }

int main () {
    int a, b = 0, c, d;
    scanf("%d", &a);
    while (sigma(b) < a) b++;
    c = a - sigma(--b);
    d = b + 2 - c;
    if (b % 2 == 0) { // 홀수
        printf("%d/%d", d, c);
    } else {
        printf("%d/%d", c, d);
    }
}