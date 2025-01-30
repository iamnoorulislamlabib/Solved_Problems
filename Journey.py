# https://codeforces.com/problemset/problem/2051/B


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
    s = sum(lst) - lst[0]
    d = lst[0]
    days = int((d + s -1)/s)
    covered = days * s
    days *= 3
    if covered - lst[3] >= d :
        days -= 1
        covered -= lst[3]
        if covered - lst[2] >= d :
            days -= 1
    print(days)
    


if __name__ == "__main__":
    redirect_io()  # Redirect only for local runs

    test_cases = 1
    test_cases = int(input())
    for tc in range(test_cases) :
        solve()
        