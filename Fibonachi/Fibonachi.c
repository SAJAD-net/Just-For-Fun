#include <stdio.h>
#include <stdlib.h>

int first=0;
int second;
int fib;
int Fibonachi(){
	for (int i=1; i<10; i++){
		printf("This is the first number => %i\n",first);
		second=first+1;
		printf("This is the second number => %i\n",second);
		fib=first+second;
		printf("--> This is the --> Fibonachi number %i\n",fib);
		first=fib;	
	}	
}		
int main(){
	Fibonachi();
}

