#include <stdio.h>
#include "ArrayList.h"

void ListInit(List * plist)
{
    (plist->__front) = 0;
    (plist->curPosition) = -1;
}

void LInsert(List * plist, LData data)
{
    if(plist->__front > LIST_LEN)
    {
        puts("저장이 불가능합니다.");
        return;
    }

    plist->arr[plist->__front] = data;
    (plist->__front)++;
}

int LFirst(List * plist, LData * pdata)
{
    if(plist->__front == 0)
        return FALSE;

    (plist->curPosition) = 0;
    *pdata = plist->arr[0];
    return TRUE;
}

int LNext(List * plist, LData * pdata)
{
    if(plist->curPosition >= (plist->__front) - 1)
        return FALSE;

    (plist->curPosition)++;
    *pdata = plist->arr[plist->curPosition];
    return TRUE;
}

LData LRemove(List * plist)
{
    int rpos = plist->curPosition;
    int num = plist->__front;
    int i;
    LData rdata = plist->arr[rpos];

    for(i=rpos; i<num-1; i++)
        plist->arr[i] = plist->arr[i+1];

    (plist->__front)--;
    (plist->curPosition)--;
    return rdata;
}

int LCount(List * plist)
{
    return plist->__front;
}