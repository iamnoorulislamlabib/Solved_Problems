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
   lst = list(map(int,input().split()))
   ans = 3
   for i in range(len(lst)) :
       x = i+1
       y = lst[lst[i]-1]
       if x == y :
           ans = 2
           break
   print(ans)

if __name__ == "__main__":
    redirect_io()  # Redirect only for local runs

    test_cases = 1
    test_cases = int(input())
    for tc in range(test_cases) :
        solve()