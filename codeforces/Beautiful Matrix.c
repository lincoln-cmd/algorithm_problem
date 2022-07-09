# include <stdio.h>
# include <stdlib.h>
 
int main(){
    int a[5][5];
    int x, y;
    for(int i = 0; i < 5; i++){
        for(int j = 0; j < 5; j++){
            scanf_s("%d", &a[i][j]);
        }
    }
    
    for(int i = 0; i < 5; i++){
        for(int j = 0; j < 5; j++){
            if(a[i][j] == 1){
                x = i, y = j;
                break;
            }
        }
    }
    
    printf("%d", abs(x - 2) + abs(y - 2));
    return 0;
}