# https://codeforces.com/problemset/problem/1966/A


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
    k = lst[1]
    lst = list(map(int,input().split()))
    dictionary = {}
    for num in lst :
        if dictionary.get(num,0) == 0 :
            dictionary[num] = 0
        dictionary[num] += 1
    
    dictionary = sorted(dictionary.items(),key= lambda item : item[1],reverse=True)
    extra = 0
    ans = 0
    for num in dictionary :
        extra += (int(num[1]/k)*(k-1))
        rem = num[1] % k
        if rem == 0 :
            continue
        need = k - rem
        if extra >= need :
            extra -= need
            extra += (k-1)
        else :
            ans += rem
    while extra >= k :
        a = int(extra/k)
        extra -= (a*k)
        extra += (a*(k-1))
    ans += extra
    print(ans)
        
        
        


if __name__ == "__main__":
    redirect_io()  # Redirect only for local runs

    test_cases = 1
    test_cases = int(input())
    for tc in range(test_cases) :
        solve()