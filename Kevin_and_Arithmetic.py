# https://codeforces.com/contest/2061/problem/A
test_case = int(input())
for t in range(test_case) :
    n = int(input())
    val = input()
    lst = list(val.split())
    
    
    ans = 0
    even = 0
    for val in lst :
        if int(val) % 2 == 0 :
            even = 1
            break
    for val in lst :
        if int(val) % 2 == 1 :
            ans += 1
    
    if not even :
        ans -= 1
    else :
        ans += 1
    
    
        
            
    print(ans)