//
// Created by 정지용 on 2021/09/28.
//
// a == 0x61 == 0d97

#include <stdio.h>
#include <stdlib.h>

long long sqt(int num, int upper) {
    if (upper == 0) return 1;
    return upper == 1 ? num : num * sqt(num, --upper) % 1234567891;
}

long long hash(char *str, int length, int count) {
    long long result = 0;
    result = (long long)(str[count] - 'a' + 1) * sqt(31, count);
    result %= 1234567891;
    return count != length ? result + hash(str, length, ++count) : 0;
}

int main() {
    int a;
    char* str;
    scanf("%d", &a);
    str = (char*) malloc(sizeof(char) * a);
    scanf("%s", str);

    printf("%lld", hash(str, a, 0) % 1234567891);
}