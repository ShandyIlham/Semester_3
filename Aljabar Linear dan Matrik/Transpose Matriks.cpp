//Tugas: Transpose Matriks
#include <iostream>
#include <conio.h>
using namespace std;

int main(){
	int i, j, m, n, matriks[10][10], transpose[10][10];
  
	cout<<" ---PROGRAM TRANSPOSE MATRIKS---"<<endl;
	cout<<"================================="<<endl;
	cout<<" Jumlah baris matriks : "; cin >> m;
	cout<<" Jumlah kolom matriks : "; cin >> n;
	
	cout << " Elemen matriks\n";
	for (i=0; i<m; i++){
		for (j=0; j<n; j++){
			cin>>matriks[i][j];
    	}
  	}
  	for (i=0; i<m; i++){
    	for (j=0; j<n; j++){
      		transpose[j][i]=matriks[i][j];
    	}
  	}
  	cout << " Hasil Transpose Matriks: \n";
  	for (i = 0; i < n; i++){
    	for (j=0; j<m; j++){
      		cout<<transpose[i][j]<<"\t";
    	}
    cout<<endl;
  	}
  	
  	getch();
  	return 0;
}
