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
    # Read all input at once
    data = sys.stdin.read().split()
    
    index = 0
    test_cases = int(data[index])
    index += 1
    results = []
    
    for _ in range(test_cases):
        n = int(data[index])
        m = int(data[index + 1])
        index += 2

        lst = list(map(int, data[index:index + n]))
        index += n

        freq = collections.defaultdict(int)
        ans = 0

        for num in lst:
            target = m - num
            if freq[target] > 0:
                ans += 1
                freq[target] -= 1
            else:
                freq[num] += 1
        
        results.append(str(ans))
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    redirect_io()
    solve()
