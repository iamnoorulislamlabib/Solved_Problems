# https://codeforces.com/problemset/problem/1957/A

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
    lst = list(map(int,input().split()))
    dictionary = {}
    for num in lst :
        if dictionary.get(num,0) == 0 :
            dictionary[num] = 0
        dictionary[num] += 1
    
    ans = 0
    for value in dictionary.values() :
        if value >= 3 :
            ans += int(value/3)
    print(ans)
        
        
        
        


if __name__ == "__main__":
    redirect_io()  # Redirect only for local runs

    test_cases = 1
    test_cases = int(input())
    for tc in range(test_cases) :
        solve()