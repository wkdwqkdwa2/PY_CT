#정확히 2개의 스펠링을 2번 사용한 문장만 구별하는 문제이다.
#정렬하는 과정을 통해 좀 더 쉽게 접근.
T=int(input())

for tc in range(T):
    A=input()
    li=[]
    li.extend(A)
    li.sort()
   
    if(li[0]==li[1] and li[2]==li[3] and li[0]!=li[2]):
        print("#{} Yes".format(tc+1))
    else:
        print("#{} No".format(tc+1))