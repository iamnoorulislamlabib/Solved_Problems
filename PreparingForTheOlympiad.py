# https://codeforces.com/problemset/problem/2051/A

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
    d = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    m = 0
    s = 0
    for day in range(d) :
        if day+1 < d :
            if a[day] > b[day+1] :
                m += a[day]
                s += b[day+1]
        else :
            m += a[day]
    ans = m - s
    print(ans)


if __name__ == "__main__":
    redirect_io()  # Redirect only for local runs

    test_cases = 1
    test_cases = int(input())
    for tc in range(test_cases) :
        solve()
        