#include "iostream"

using namespace std;
int num;
int tringle;

bool isTringular(int num){
    if (num < 0){
        return false;
    }

    int sum ;
    for (int n=1; sum<=num; n++){
        sum = sum + n;
        if (sum == num){
            return true;
        }
    }
    return false;

}
int main(){
    cout << "enter your number :";
    cin >> num;
    if (isTringular(num)){
        cout <<"This is a tringular number";
        return 0;
    }else{
        cout << "This is not tringular number";
    }
}
