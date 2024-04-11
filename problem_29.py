#2072 홀수만 더하기

T=int(input())

for test_case in range(T):
    number=list(map(int,input().split()))
    number_sum=0
    for i in range(10):
        if number[i]%2==1:
            number_sum+=number[i]
    print("#{} {}".format(test_case+1,number_sum))