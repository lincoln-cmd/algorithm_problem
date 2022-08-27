#include <stdio.h>
#include <iostream>

using std::cin;
using std::cout;
using std::endl;
using std::string;

int main(){
    int n, x = 0;
    cin >> n;
    string s;
    for(int i = 0; i < n; i++){
        cin >> s;
        if(s[0] == '+' || s[s.length() - 1] == '+'){
            x++;
        }else{
            x--;
        }
    }
    cout << x << endl;
    
    return 0;
}