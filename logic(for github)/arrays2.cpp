#include <iostream>

using namespace std;

int main(){

    int finishedrow1[3];
    int finishedrow2 [3];

    int test[2][3] = {{4,3,2},{345,14,23}};

    for(int i =0;i<2;i++){

        for(int x=0;x<3;x++){

            while(i == 1){

                int num = test[i][x];
                finishedrow2[x] = num;
                break;


            }


            while(i == 0){
                int num2 = test[i][x];

                finishedrow1[x] = num2;


                break;


            }

        }

    }

    for(int i = 0;i<3; i++){
        cout << finishedrow1[i] << ' ' << endl;
        cout << finishedrow2[i] << ' ';
    }


}
