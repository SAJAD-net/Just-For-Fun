#include "iostream"

using namespace std;

int num;
int even(int num){
     int factorial=1;
    for (int a=1; a<=num; a++){
        factorial=factorial*a;
    }
    cout << "This is a factorial of number :"<<num<<" --> "<<factorial<<endl;
    return 0;
}

int odd(int num){
    for (int i=0; i <= num; i++){
       for (int x=1; x<=num-1; x++){
           cout<<" ";
       }
       for(int j=1; j <2*i; j++){
            cout<<"@";
       }         
       cout<<endl;
    }
   return 0;
}


int und(int num){

    if (num % 2 == 0){
        even(num);
    }else{
        odd(num);
    }
}
int main(){
    cout<<"Enter a number :";
    cin >> num;
    und(num);
    return 0;
}