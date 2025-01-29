# https://codeforces.com/problemset/problem/2060/A

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
    lst = list(map(int, input().split()))
    ans = 0
    d = {}
    for temp in range(-200,201) :
        d[temp] = 0
        if lst[0] + lst[1] == temp :
            d[temp] += 1
        if lst[1] + temp == lst[2] :
            d[temp] += 1
        if temp + lst[2] == lst[3] :
            d[temp] += 1
    
    ans = max(d.values())
    print(ans)


if __name__ == "__main__":
    redirect_io()  # Redirect only for local runs

    test_cases = 1
    test_cases = int(input())
    for tc in range(test_cases) :
        solve()
        