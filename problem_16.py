T=int(input())

for tc in range(T):
    A,B=map(int,input().split())
    result=A*B
    if(A>9 or B>9):
        result=-1
    print("#{} {}".format(tc+1, result))