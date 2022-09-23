// Tugas: Pembagian Matriks
#include <iostream>
#include <conio.h>
using namespace std;

int main(){
	int i, j, m, n, skalar, matriksA[10][10], hasil[10][10];
  
	cout << " --PROGRAM PERKALIAN SKALAR MATRIKS--" << endl;
	cout << "=====================================" << endl;
	cout << " Jumlah baris matriks : "; cin >> m;
	cout << " Jumlah kolom matriks : "; cin >> n;
	
	cout << endl;
	cout << " Masukkan Nilai Pengali : "; cin >> skalar;
  	cout << " Matrix A : \n";
	for(i=0; i<m; i++){
		for(j=0; j<n; j++){
      		cin>>matriksA[i][j];
    	}
  	}
  	cout<<" Hasil pengurangan matrix : \n";
  	for(i=0; i<m; i++){
    	for(j=0; j<n; j++){
      		hasil[i][j]=skalar*matriksA[i][j];
      		cout<<hasil[i][j]<<"\t";
    	}
    cout<<endl;
	}
  
	getch();
	return 0;
}
