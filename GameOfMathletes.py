import sys
import os
import collections


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
    n,m=map(int,input().split())
    lst = list(map(int,input().split()))
    freq = collections.defaultdict(int)
    ans = 0
    for num in lst :
        target = m - num
        if freq[target] > 0 :
            ans += 1
            freq[target] -= 1
        else :
            freq[num] += 1
    
    print(ans)
        

if __name__ == "__main__":
    redirect_io()
    test_cases = int(input())
    for _ in range(test_cases):
        solve()
