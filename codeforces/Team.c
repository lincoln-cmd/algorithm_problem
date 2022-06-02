#include <stdio.h>

int main(){
    int n, cnt = 0;
    scanf("%d", &n);
    int P, V, T;
    for (int i = 0; i < n; i++){
        scanf("%d %d %d", &P, &V, &T);
        if (P == 1){
            if (V == 1 || T == 1){
                cnt++;
            }
        }else if(V == 1 && T == 1){
            cnt++;
        }
    }
    printf("%d", cnt);
    return 0;
}