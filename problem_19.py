#"A", "B", "C"의 3가지 알파벳으로 이루어진 문자열 original이 주어집니다. 
#이때 연속으로 여러 번 사용된 문자는 문자와 연속된 횟수로 압축할 수 있습니다. 
#예를 들어 문자열 "AAABCCC"는 "A3B1C3"으로 나타낼 수 있습니다. original을 입력받아 압축된 문자열을 return하는 solution 함수를 작성해주세요.
# 단 변환된 문자열의 길이가 original보다 길다면 original을 return해야 합니다.

#핵심방법 인덱스의 종류와 그것들의 개수(Count)를 응용
T=int(input())

for tc in range(T):
    A=input()
    ls=[]
    count=0

    for le in range(len(A)-1): #아래 코드에 대한 오류를 방지하기 위해 -1를 진행 < 개선점 1,부터 길이만큼 진행한다면 코드를 좀 더 짧게 구현가능
        if A[le]==A[le+1]: #다음 문자와 같으면 count를 통해 해당 문자의 개수
            count+=1            
        else: #다음 문자와 다를 경우 실행           
            #여태까지 구한 문자와 그 문자의 개수 리스트에 저장
            ls.append(A[le])
            ls.append(count+1)            
            count=0
            #마지막 문자가 하나만 있을 때를 위한 if문
            if le==len(A)-2 and A[le]!=A[le+1]:
                ls.append(A[le+1])            
                ls.append(count+1)
            
    print(ls)