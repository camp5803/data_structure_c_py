//
// Created by 정지용 on 2021/09/30.
//

#include <stdio.h>

int main() {
    int n, m, temp, res = 0;
    int c[100] = {0,};
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++) {
        scanf("%d", &c[i]);
    }

    for (int i = 0; i < n - 2; i++) {
        for (int j = i + 1; j < n - 1; j++) {
            for (int k = j + 1; k < n; k++) {
                temp = c[i] + c[j] + c[k];
                if (temp <= m && temp > res) {
                    res = temp;
                }
            }
        }
    }
    printf("%d", res);
}