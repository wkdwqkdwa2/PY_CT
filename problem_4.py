# 퀴즈 대회에 참가해서 우승을 하게 되면 보너스 상금을 획득할 수 있는 기회를 부여받는다.
# 우승자는 주어진 숫자판들 중에 두 개를 선택에서 정해진 횟수만큼 서로의 자리를 위치를 교환할 수 있다.
# 예를 들어, 다음 그림과 3, 2, 8, 8, 8 의 5개의 숫자판들이 주어지고 교환 횟수는 2회라고 하자.

T=int(input())

for test_case in range(T):
    A,B=input().split()
    B=int(B)
    A = list(map(int, A))
    for b in range(B):
        index=0
        for c in range(b+1, len(A)):            
            if(A[index]<=A[c]):
                index=c

        A[index], A[b]=A[b],A[index]
    result  = ''.join(map(str, A))
    print("#{0}".format(test_case + 1), result )
    