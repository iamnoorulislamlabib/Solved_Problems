# https://codeforces.com/contest/2053/problem/A
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
    for i in range(n-1) :
        if 2*lst[i] > lst[i+1] and lst[i] < 2*lst[i+1] :
            print("YES")
            return
    
    
    print("NO")          
         
    


if __name__ == "__main__":
    redirect_io()  # Redirect only for local runs

    test_cases = 1
    test_cases = int(input())
    for tc in range(test_cases) :
        solve()
        