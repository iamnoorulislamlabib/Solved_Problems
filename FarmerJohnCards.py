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
    n, m = map(int, input().split())
    mat = []
    
    for i in range(n):
        temp = list(map(int, input().split()))
        temp.sort()  # Sort in ascending order
        mat.append([i] + temp)  # Ensure i is added AFTER sorting

    mat = sorted(mat, key=lambda row: row[1])  # Sort rows by column index 1

    mn = -1
    for j in range(1, m+1):
        if j != 1:
            mn = mat[n-1][j-1]
        for i in range(n-1):  # Fix the loop range
            if i == 0 and mat[i][j] < mn:
                print(-1)
                return
            if mat[i][j] > mat[i+1][j]:
                print(-1)
                return

    print(" ".join(str(row[0]+1) for row in mat))

if __name__ == "__main__":
    redirect_io()
    test_cases = int(input())
    for _ in range(test_cases):
        solve()
