//
// Created by 정지용 on 2021/08/27.
//
#include <stdio.h>
#include <stdlib.h>
#include "ArrayList.c"
#include "03-2_prob.h"
#include <string.h>

nameCard * makeNameCard(char * name, char * phone) {
    nameCard * pcard = (nameCard *) malloc(sizeof(nameCard));
    strcpy(pcard->name, name);
    strcpy(pcard->phone, phone);

    return pcard;
}

void showNameCardInfo(nameCard * pcard) {
    printf("[>] 이름: %s\n", pcard->name);
    printf("[>] 전화번호: %s\n", pcard->phone);
}

int nameCompare(nameCard * pcard, char * name) {
    if (!strcmp(pcard->name, name))
        return 0;
    return -1;
}

void changePhoneNum(nameCard * pcard, char * phone) {
    strcpy(pcard->phone, phone);
}

void line() {
    printf("\n================================\n\n");
}

void printMenu() {
    line();
    printf("[*] 1번은 전체 출력\n");
    printf("[*] 2번은 특정 이름 검색 및 출력\n");
    printf("[*] 3번은 특정 이름 검색 및 전화번호 변경\n");
    printf("[*] 4번은 특정 이름 검색 및 정보 삭제\n");
    printf("[*] 5번은 escape\n");
    printf("[<] 입력: ");
}

int main() {
    List list;
    nameCard * pcard;
    printf("%lu %lu", sizeof(nameCard), sizeof(pcard));
    int menu;
    char tname[NAME_LEN];
    char tphone[PHONE_LEN];

    ListInit(&list);

    for (int i = 0; i < 3; i++) {
        printf("[<] 이름과 전화번호 순으로 입력: ");
        scanf("%s %s", tname, tphone);
        pcard = makeNameCard(tname, tphone);
        LInsert(&list, pcard);
    }

    while (TRUE) {
        printMenu();
        scanf("%d", &menu);
        line();
        switch (menu) {
            case 1:
                if (LFirst(&list, &pcard)) {
                    showNameCardInfo(pcard);
                    while (LNext(&list, &pcard)) {
                        showNameCardInfo(pcard);
                    }
                }
                break;
            case 2:
                printf("[<] 검색할 이름 입력: ");
                scanf("%s", tname);
                if (LFirst(&list, &pcard)) {
                    nameCompare(pcard, tname) ? : showNameCardInfo(pcard);
                    while (LNext(&list, &pcard)) {
                        nameCompare(pcard, tname) ? : showNameCardInfo(pcard);
                    }
                }
                break;
            case 3:
                printf("[<] 검색할 이름 입력: ");
                scanf("%s", tname);
                if (LFirst(&list, &pcard)) {
                    if (!nameCompare(pcard, tname)) {
                        printf("[*] 검색 성공! \n");
                        printf("[<] 변경할 전화번호 입력: ");
                        scanf("%s", tphone);
                        changePhoneNum(pcard, tphone);

                        printf("[*] 변경 성공! \n");
                        showNameCardInfo(pcard);
                    }
                    while (LNext(&list, &pcard)) {
                        if (!nameCompare(pcard, tname)) {
                            printf("[*] 검색 성공! \n");
                            printf("[<] 변경할 전화번호 입력: ");
                            scanf("%s", tphone);
                            changePhoneNum(pcard, tphone);

                            printf("[*] 변경 성공! \n");
                            showNameCardInfo(pcard);
                        }
                    }
                }
                break;
            case 4:
                printf("[<] 검색할 이름 입력: ");
                scanf("%s", tname);
                if (LFirst(&list, &pcard)) {
                    if(!nameCompare(pcard, tname)) {
                        pcard = LRemove(&list);
                        free(pcard);
                        printf("[*] 삭제 성공! \n");
                    }
                    while (LNext(&list, &pcard)) {
                        if(!nameCompare(pcard, tname)) {
                            pcard = LRemove(&list);
                            free(pcard);
                            printf("[*] 삭제 성공! \n");
                        }
                    }
                }
                break;
            case 5:
                return 0;
            default:
                printf("[*] 잘못된 입력입니다. 다시 입력해주세요. \n");
                break;
        }
    }
}