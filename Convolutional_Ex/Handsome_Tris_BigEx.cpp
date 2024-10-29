#include <iostream>
#include <string.h>
#include <iomanip>

using namespace std;

int main(){
    int m,n,p,q,sum=0;
    cout << "input m: ";
    cin >> m;
    cout << "input n: ";
    cin >> n;
    cout << "input p: ";
    cin >> p;
    cout << "input q: ";
    cin >> q;
    int keras[p][q];
    int source[m][n];
    if (m<p || n<q){
        cout << "You dumb AF, GET OUT !" << endl;
    }
    else{
        cout << "Input source !" << endl;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++){
                cout << "Row " << i+1 << ", Column " << j+1 << " : "; 
                cin >> source[i][j];
            }
        }
        cout << "Input kernel !" << endl;
        for (int i = 0; i < p; i++){
            for (int j = 0; j < q; j++){
                cout << "Row " << i+1 << ", Column " << j+1 << " : "; 
                cin >> keras[i][j];
            }
        }

        if (m==p && n==q){
            for (int i = 0; i < p; i++){
                for (int j=0; j < q; j++){
                    sum += source[i][j] * keras[i][j];
                }
            }
            cout << "Output: " << sum << endl;
        }
        else {
            int result[m-p+1][n-q+1];
            int cor=0, sair=0;
            while (1){
                sum = 0;
                for (int i = 0; i < p; i++){
                    for (int j=0; j < q; j++){
                        sum += source[i + cor][j + sair] * keras[i][j];
                    }
                }
                result[cor][sair] = sum;
                if (p + sair == m){
                    sair = 0;
                    if (q + cor == n){
                        cout << "Thanh !!!!!!!!!!!!" << endl;
                        break;
                    }
                    cor += 1;
                }
                else{
                    sair++;
                }
            }
            for (int i = 0; i < m-p+1; i++){
                for (int j = 0; j < n-q+1; j++){
                    cout << setw(4) << result[i][j] << " ";
                }
                cout << endl;
            }
        }
    }
    return 0;
}