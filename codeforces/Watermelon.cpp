#include <stdio.h>
#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int main(){
    
	int w;
    cin >> w;
    
    if(w != 2 && w % 2 == 0){
        cout << "YES" << endl;
    }else{
        cout << "NO" << endl;
    }
    
    return 0;
}