#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool solution(int x) {
    bool answer = true;
    
    int a, b = 0;
    a = x;
    while (a > 0){
        b += (a % 10);
        a /= 10;
    }
    
    if (x % b == 0){
        return answer;
    }else {
        return false;
    }
    return 0;
}