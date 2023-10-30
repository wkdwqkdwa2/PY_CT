#캡처를 했을 때, 파일명으로 정렬하기

#시작하기전 핵심 요소! 먼저 앞에 숫자가 1일때를, 고려하면서 그다음은 1 > 10 > 11 > 12
T=int(input())

for tc in range(T):
    A=input()
    TEN=len(A) #이 문장을 통해 입력한 값들이 몇자리 수 인지 파악
    #몇자리 수 까지 확인 후 100자리라면 백자리와, 십의자리 수까지 파악한다 EX)1, 10?, 11?, 12?
    num=1
    A=int(A)
    for an in range(A):
        
        #앞부분이 1, 10 , 100.. 시작하는 부분 해결
        if(TEN>1):
            num*=10
            TEN-=1        
        elif(num<A):
            if(num%10==9):
                num+=1
                num//=10
            elif(num%10!=9):
                num+=1
        elif(num==A):
            num//=10

             