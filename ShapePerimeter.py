# https://codeforces.com/problemset/problem/2056/A


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
    lst = list(map(int,input().split()))
    n,m = lst[0],lst[1]
    x,y = 0,0
    p,q = 0,0
    for i in range(n) :
        lst = list(map(int,input().split()))
        if i == 0 :
            x,y = lst[0],lst[1]
            p,q = x,y
        else :
            p += lst[0]
            q += lst[1]
    p += m
    q += m
    ans = 2*(p-x + q-y)
    print(ans)
        
                    
        
         
    


if __name__ == "__main__":
    redirect_io()  # Redirect only for local runs

    test_cases = 1
    test_cases = int(input())
    for tc in range(test_cases) :
        solve()
        