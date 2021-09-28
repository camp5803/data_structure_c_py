//
// Created by 정지용 on 2021/09/28.
//

#include <stdio.h>
#include <string.h>
#define true 1

int main() {
    char input[5] = {0, };
    int stat = 0;
    while (true) {
        scanf("%s", input);
        if (strlen(input) == 1) stat = 1;
        if (!strcmp(input, "0")) break;
        for (int i = 0; i < strlen(input) / 2; i++) {
            if (input[i] != input[strlen(input) - i - 1]) {
                stat = 0;
                break;
            } else
                stat = 1;
        }
        stat ? printf("yes\n") : printf("no\n");
    }
}