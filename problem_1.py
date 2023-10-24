

T = int(input())
for test_case in range(1, T + 1):
    count=0
    a, b = map(int, input().split())
    if a==b:
        count=0
    elif a+1==b:
        count=-1
    else:
        count=(b-a)//2
    print("#"+str(test_case+1),count)