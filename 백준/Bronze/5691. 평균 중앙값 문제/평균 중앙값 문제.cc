#include <iostream>
#include <vector>

using namespace std;


int main() {

    while (true) {
        int a, b;
        cin >> a >> b;

        if (a == 0 && b == 0) {
            break;
        }
        
        cout << ((a * 3) - (a + b)) << endl;
    }
    
    return 0;
}