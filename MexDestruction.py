# https://codeforces.com/problemset/problem/2049/A

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
    n = int(input())
    lst = list(map(int,input().split()))
    i,j = -1,-1
    for idx in  range(n) :
        if lst[idx] != 0 and i == -1 :
            i = idx
        if lst[idx] != 0 :
            j = idx
    
    if i == -1 :
        print(0)
        return
    flag = False
    for idx in range(i,j+1) :
        if lst[idx] == 0 :
            flag = True
    if flag :
        print(2)
    else :
        print(1)
        
           
         
    


if __name__ == "__main__":
    redirect_io()  # Redirect only for local runs

    test_cases = 1
    test_cases = int(input())
    for tc in range(test_cases) :
        solve()
        