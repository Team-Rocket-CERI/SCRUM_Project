nclude<iostream>
#include<time.h>
using namespace std;

int main(){

		int  count = 0;
			clock_t c = clock();
				for(int i=0; i<10000; i++){
							for(int j=0; j<10000; j++){
											count++;	
													}
								}
					c = clock() - c;
						cout<<((float)c)/CLOCKS_PER_SEC<<endl;
}
