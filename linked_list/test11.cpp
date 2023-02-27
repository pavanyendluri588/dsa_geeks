
/*
1
23
4 4 1 4 13 8 8 8 0 8 14 9 15 11 -1 10 15 22 22 22 22 22 21
output:22


https://leetcode.com/discuss/interview-question/2032859/Juspay-or-OA-or-Maximum-Weight-Node



https://onlinegdb.com/_bQMOyZSA

*/






/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
#include <math.h>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int solution(vector<int>arr){
    int ans=INT_MIN;
    int result=-1;
    vector<int>weight(arr.size(),0);
    for(int i=0;i<arr.size();i++){
        int source=i;
        int dest=arr[i];
        if(dest!=-1){
            weight[dest]+=source;
            if(ans<=weight[dest]){
                ans=max(ans,weight[dest]);
                result=dest;
            }
            
        }
    }
    if(ans!=INT_MIN)
        return result;
    return -1;
}

int main(int argc, char **argv)
{
    int testcases;
    cin >> testcases;
    while(testcases--){ 
        int array_size;
        cin >> array_size;
         vector<int> arr(array_size);
         for (int i=0; i<array_size; i++){
cin >> arr[i];
         }
         cout <<"11"<< solution (arr) << endl;
         }
         return 0;
         }

