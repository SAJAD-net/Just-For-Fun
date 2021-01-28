#include <stdio.h>

int count=0;
int i;
int from,to;
char s;
int even(){
	puts("** WELCOME TO EVEN PRINTER **\n");
	printf("OK, enter the number to from of range ~$ ");
	scanf("%i",&from);
	puts("OK");
	printf("Enter the number to end of range ~$ ");
	scanf("%i",&to);
	for (i=from; i<to; i++){
		if (i%2 == 0){
			printf("%i ",i);
			count++;
//			return 1;
		}
		else
//			return 0;
			puts(" ");
	}
	printf("\nThis is the count of even number on range --> %i : %i to %i\n",count,from,to);
}

int main(){
	even();
}
