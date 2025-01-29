# https://codeforces.com/problemset/problem/1956/A

import sys
import os

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
    lst = list(map(int,input().split()))
    mn = lst[0]
    lst = list(map(int,input().split()))
    ans = []
    for num in lst :
        if num < mn :
            ans.append(num)
        else :
            ans.append(mn-1)
    
    print(*ans) # to print the whole line together
        
        


if __name__ == "__main__":
    redirect_io()  # Redirect only for local runs

    test_cases = 1
    test_cases = int(input())
    for tc in range(test_cases) :
        solve()