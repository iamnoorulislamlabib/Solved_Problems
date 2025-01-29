# https://codeforces.com/problemset/problem/1972/A

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
    _ = input()
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    operation = 0
    i = 0
    j = 0
    while j < len(b) :
        if a[i] <= b[j] :
            i += 1
            j += 1
        else :
            operation += 1
            j += 1
    print(operation)


if __name__ == "__main__":
    redirect_io()  # Redirect only for local runs

    test_cases = 1
    test_cases = int(input())
    for tc in range(test_cases) :
        solve()
        