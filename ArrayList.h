#ifndef __ARRAY_LIST_H__
#define __ARRAY_LIST_H__

#define TRUE	1
#define FALSE	0
#include "03-2_prob.h"

/*** ArrayList의 정의 ****/
#define LIST_LEN	100
// typedef int LData;
typedef nameCard* LData;

typedef struct __ArrayList
{
    LData arr[LIST_LEN];
    int __front;
    int curPosition;
} ArrayList;


/*** ArrayList와 관련된 연산들 ****/
typedef ArrayList List;

void ListInit(List * plist);
void LInsert(List * plist, LData data);

int LFirst(List * plist, LData * pdata);
int LNext(List * plist, LData * pdata);

LData LRemove(List * plist);
int LCount(List * plist);

#endif