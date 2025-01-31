# https://codeforces.com/contest/2060/problem/B


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
    n,m = lst[0],lst[1]
    if n == 1 :
        print(1)
        return
    dictionary = {}
    for i in range(n) :
        lst = list(map(int,input().split()))
        for num in lst :
            dictionary[num] = i
    lst = dict(sorted(dictionary.items(),key= lambda item : item[0] ))
    freq = {}
    i = 0
    for value in lst.values() :
        if i == n :
            break
        if freq.get(value,0) == 0 :
            freq[value] = 0
        freq[value] += 1
        if freq[value] == 2 :
            print(-1)
            return
        i += 1
    
    


if __name__ == "__main__":
    redirect_io()  # Redirect only for local runs

    test_cases = 1
    test_cases = int(input())
    for tc in range(test_cases) :
        solve()
        