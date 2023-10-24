import math

T=int(input())

for test_case in range(T):
    I=int(input())
    x=0
    y=0
    #처음 에는 입력하는 값의 절반으로 나눈 뒤 그 범위에서 for문을 돌렸지만, 시간적 문제로 제곱근을 이용하여 해결 math.sqrt()
    #제곱근의 특성상 나온 값 기준으로 약수의 개수가 대칭을 이루는 것을 이용
    for i_case in range(1,int(math.sqrt(I))+1):
        
        if(I%i_case==0):
            x=i_case         
    y=I/x
    result=x+y-2
    print("#{0} {1}".format(test_case+1,int(result)))