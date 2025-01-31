# https://codeforces.com/contest/2060/problem/B


import sys
import os
import math

def is_online_judge():
    return os.getenv("ONLINE_JUDGE") is not None  # Some OJs set this


def redirect_io():
    """Redirects I/O only if running locally."""
    if not is_online_judge():  
        try:
            sys.stdin = open("input.txt", "r")
            sys.stdout = open("output.txt", "w")
        except FileNotFoundError:
            pass




def solve():
    n,m=map(int,input().split())
    mat = []
    for i in range(n) :
        temp = list(map(int,input().split()))
        temp.sort(reverse=False)
        temp = [i] + temp
        mat.append(temp)
    
    mat = sorted(mat,key=lambda row : row[1])
    for j in range(1,m+1) :
        for i in range(0,n-1) :
            if mat[i][j]>mat[i+1][j] :
                
        
    
    


if __name__ == "__main__":
    redirect_io()  # Redirect only for local runs

    test_cases = 1
    test_cases = int(input())
    for tc in range(test_cases) :
        solve()
        