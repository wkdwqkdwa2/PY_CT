T = int(input())
for test_case in range(T):
    h = input()
    for t in range(1,len(h)):
        a=int(h[:t])
        b=int(h[t:])
        sum=a+b
        if(t==1):
            min=sum
        if(sum<min):
            min=sum
    print("#{0}".format(test_case+1), min)