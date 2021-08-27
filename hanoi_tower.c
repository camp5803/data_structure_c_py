//
// Created by 정지용 on 2021/08/27.
//

// 3개의 원반이 있다는 전제; 윤성우의 열혈 자료구조

#include <stdio.h>

void moveDisks(int height, char from, char by, char to);

int main() {
    moveDisks(3, 'A', 'B', 'C');
}

void moveDisks(int height, char from, char by, char to) {
    if (height == 1) {
        printf("move disk %c to %c\n", from, to);
    } else {
        moveDisks(height - 1, from, to, by);
        printf("move disk %d %c to %c\n", height, from, to);
        moveDisks(height - 1, by, from, to);
    }
}