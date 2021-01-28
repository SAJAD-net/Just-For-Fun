
#include <iostream>
#include <iomanip>
//#include <conio.h>
#define n 10

using namespace std;

int v[n+1],board[n][n],counter;
int nqueens;

void clearBoard()
{
	int row, col;
	for(row=0;row<n;row++)
   	for(col=0;col<n;col++)
      	board[row][col]=0;
}

int drawBoard()
{

   clearBoard();

   	for(int i=1 ; i<nqueens+1 ; i++)
   		board[i-1][v[i]-1]=1;

   	cout<<"\n["<<++counter<<"]"<<endl<<endl;

   	for(int row=0 ; row<nqueens ; row++)
	{
      for(int col=0 ; col<nqueens ; col++)
        	if(board[row][col]==1)
         		cout<<setw(3)<<'X';
       		else
         		cout<<setw(3)<<'-';
      cout<<endl<<endl;
   	}
	return 0;
}

int isSafe(int row,int col)
{
	int i;
  	for(i=1 ; i<row ; i++)
   {
   	if(v[i]==col || i-v[i]==row-col || i+v[i]==row+col)
      	return 0;
	else
		return 1;
   }

}
int findQueen(int row,int nqueens)
{
	int col;
  	for(col=1 ; col<=nqueens ; col++)
   		if(isSafe(row,col))
    	{
    	  	v[row]=col;
    	  	if(row==nqueens){
    	        drawBoard();
				return 0;
			}
			
    	  	//else if (row > nqueens){
			//	  int tmp = row;
			//	  tmp -= nqueens;
			//	  row -= tmp;
			//	  row = nqueens;
			//	  findQueen(row,nqueens);
			//}
			else if (row < nqueens){
				char s;
				row++;
				cout << row << nqueens << endl;
				cin >> s;
				findQueen(row,nqueens);
			}
			//else if (row > nqueens){
			//	return 0;
			//	int tm;
			//	char s;
			//	tm = row;
			//	tm -= nqueens;
			//	row -= tm;
			//	cout << row << nqueens << endl;
			//	cin >> s;
			//	findQueen(row,nqueens);

			//}
			//findQueen(row+1,nqueens);
			//cout << "This number is grate !" << endl;
			else{
				int t;
				cin >> t;
			}
		}
}
//main function must be return int
int main()
{
  	cout<<"Please enter number of Queens [9>n>=4]: ";
  	cin>>nqueens;
	cout <<nqueens<<endl;
	findQueen(1,nqueens);
//   	getch();
//	system("pause");
	return 0;
}
