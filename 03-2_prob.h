//
// Created by 정지용 on 2021/08/27.
//

#ifndef DATA_STRUCTURE_CLANG_03_2_PROB_H
#define DATA_STRUCTURE_CLANG_03_2_PROB_H

#define NAME_LEN    30
#define PHONE_LEN   30

typedef struct __namecard {
    char name[NAME_LEN];
    char phone[PHONE_LEN];
} nameCard;

nameCard * makeNameCard(char * name, char * phone);
void showNameCardInfo(nameCard * pcard);
int nameCompare(nameCard * pcard, char * name);
void changePhoneNum(nameCard * pcard, char * phone);

#endif //DATA_STRUCTURE_CLANG_03_2_PROB_H
