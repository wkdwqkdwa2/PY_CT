T=int(input())

for tc in range(T):
    a,b=map(int, input().split())
    time=a+b
    
    if(24<=time):
        time=time-24
        
    print("#{} {}".format(tc+1, time))