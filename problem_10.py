T=int(input())

for tc in range(T):
    N=int(input())
    if(N%2==0):
        print("#{} Alice".format(tc+1))
    elif(N%2==1):
        print("#{} Bob".format(tc+1))