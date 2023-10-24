#순서가 정해져 있는 걸 파악 후 짝수면 Alice, 홀수면 Bob이 이긴다는 결론을 도출.
T=int(input())

for tc in range(T):
    N=int(input())
    if(N%2==0):
        print("#{} Alice".format(tc+1))
    elif(N%2==1):
        print("#{} Bob".format(tc+1))