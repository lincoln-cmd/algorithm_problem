#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int num) {
    int cnt = 0;
    long num2 = num;
    while (num2 != 1){
        (num2 % 2 == 0) ? (num2 /= 2) : (num2 = num2 * 3 + 1);
        cnt++;
        if (cnt > 500) return -1;
    }
    return cnt;
}