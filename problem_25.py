
T=int(input())

for tc in range(T):    
    n,m=map(int,input().split())
    ls=[]

    for A in range(n):
        ls.append(list(input()))
    result=0
    
    for a in range(n-1): #행검사        
        if ls[a][0]!=ls[a+1][0] or ls[a+1][0]=='?':
            if ls[a+1][0]=='?':
                if ls[a][0]=='.':
                    ls[a+1][0]=='#'
                elif ls[a][0]=='#':
                    ls[a+1][0]=='.'
            result+=1
            for b in range(m-1): #열검사
                if ls[a][b]!=ls[a][b+1] and ls[a][b+1]=='?':
                    result+=1
                elif ls[a][b]==ls[a][b+1]:
                    break
    if result==n+m-2:
        print("#{} possible".format(tc+1))
    else:
        print("#{} impossible".format(tc+1))