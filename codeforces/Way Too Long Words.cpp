#include <stdio.h>
#include <iostream>

using std::cin;
using std::cout;
using std::endl;
using std::string;

int main(){
    int n;
    string s;
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> s;
        if(s.length() > 10){
            cout << s[0] << s.length() - 2 << s[s.length() - 1] << endl;
        }else{
            cout << s << endl;
        }
    }
    return 0;
}