#include <stdio.h>
 
int main(){
    int m, n;
    scanf("%d %d", &m, &n);
    int cnt = 0;
    
    int a = m / 2, b = m % 2;
    int c = n / 2, d = n % 2;
    
    printf("%d", a * n + b * c);
    return 0;
}