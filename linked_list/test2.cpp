


/*
HERE IS THE QUESTION, WHAT IS THE LOGIC AND CODE TO SOLVE THIS QUESTION ??
You are given a maze with N cells. Each cell may have multiple entry points but not more than one exit (ie. entry/exit points are unidirectional doors like valves).

The cells are named with an integer value from 0 to N-1.

You need to find the the length of the largest cycle in the maze. Return -1 if there are no cycles.

INPUT FORMAT

First line has the number of cells N
Second line has list of N values of the edge[] array. edge[i] contains the cell number that can be reached from of cell ‘i’ in one step. edge[i] is -1 if the ‘i’th cell doesn’t have an exit.
OUTPUT FORMAT

length of the largest cycle.
Sample input:

23

4 4 1 4 13 8 8 8 0 8 14 9 15 11 -1 10 15 22 22 22 22 22 21

Sample output

6


*/

#include <iostream>
#include <math.h>
#include <vector>
#include <bits/stdc++.h>

using namespace std;


int solve(vector<int>& maze,int n)
{
    int maxSum=-1;

    for(int i=0; i<n; i++)
    {
        int node=i;  
        int sum=0;
        unordered_set<int> visited;

        while(node < n && node >= 0 && i!=maze[node] && visited.count(node)==0)
        {
            visited.insert(node);
            sum+=node;
            node=maze[node];            
        }

        if(node>=0  && node < n && i == maze[node])
        {
            maxSum=max(maxSum,sum);
        }
    }

    return maxSum;
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
         cout <<"11"<< solve (arr) << endl;
         }
         return 0;
         }

