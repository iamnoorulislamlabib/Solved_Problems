# https://codeforces.com/problemset/problem/1968/B

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
    _ = input()
    str1 = input()
    str2 = input()
    a = 0
    b = 0
    ans = 0
    while a < len(str1) and b < len(str2) :
        if str1[a] == str2[b] :
            ans += 1
            a += 1
            b += 1
        else :
            b += 1
    
    print(ans)
    

if __name__ == "__main__":
    redirect_io()  # Redirect only for local runs

    test_cases = 1
    test_cases = int(input())
    for tc in range(test_cases) :
        solve()