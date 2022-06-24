#include <stdio.h>

int main(){
    int n, k, cnt = 0;
    scanf("%d %d", &n, &k);
    
    int arr[n];
    for (int i = 0; i < n; i++){
        scanf("%d", &arr[i]);
    }
    
    for (int j = 0; j < n; j++){
        if (arr[j] >= arr[k - 1] && arr[j] > 0){
            cnt++;
        }
    }
    
    printf("%d\n", cnt);
    return 0;
}