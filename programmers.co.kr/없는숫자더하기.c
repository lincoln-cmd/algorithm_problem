#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// numbers_len은 배열 numbers의 길이입니다.
int solution(int numbers[], size_t numbers_len) {
    int answer = 0;
    int total = 0;
    int sum = 0;
    
    for (int a = 0; a < 10; a++){
        total += a;
    } // 0~9까지 총합
    
    for (int i = 0; i < numbers_len; i++){
        sum += numbers[i];
    } // 배열 numbers의 총합
    
    
    answer = total - sum;
    
    return answer;
}