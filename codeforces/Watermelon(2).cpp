// utilize switch/case

#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int main(){
    int w, value;
    cin >> w;
    value = w % 2;
    switch(value){
        case 0:
            switch(w){
                case 2:
                    cout << "NO" << endl;
                    break;
                default:
                    cout << "YES" << endl;
            }
            break;
        default:
            cout << "NO" << endl;
    }
    return 0;
}




// utilize ternary operator

#include <iostream>


using std::cin;
using std::cout;
using std::endl;

int main(){
    int w;
    cin >> w;
    
    cout << ((w != 2 && w % 2 == 0) ? "YES" : "NO") << endl;
    
    
    return 0;
}