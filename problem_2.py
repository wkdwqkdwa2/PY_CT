#  성재는 두 개의 자연수 a와 b를 더하기 위해 컴퓨터를 켜고 계산기에 “a+b”를 입력하였다. 하지만 계산기 앱의 버그로 인해 덧셈 키 ‘+’가 제대로 입력되지 않아, 
#화면에는 a+b 값 대신에 a와 b를 이어붙인 값이 적혀 있게 되었다. 예를 들어 a = 174, b = 3이었다면, 계산기 화면에 “1743”이 나타나 있었을 것이다. 
#성재는 ‘+’ 키가 제대로 동작하지 않는 것을 알았지만 ‘나중에 다시 입력하면 되겠지’라고 생각하고는 읍내로 외출을 하였다.
#  몇 시간 뒤, 컴퓨터 앞으로 돌아온 성재는 자신이 계산기 화면에 “a+b”를 입력하려고 하였으나, 
#계산기 앱의 버그로 인해 화면에는 a+b 값 대신에 a와 b를 이어 붙인 값이 적혀 있게 되었다는 사실은 기억했지만, a와 b의 값 자체는 기억하지 못했다. 예를 들어 성재가 “1743”을 보았다면, 
#자신이 “1+743”, “17+43”, “174+3” 중 무엇을 입력하려고 했는지 기억하지 못하는 것이다.
#  성재는 어쩔 수 없이, 가능한 모든 경우 가운데 계산 결과가 가장 작은 것을 구해 보기로 하였다. 예를 들어 위의 경우 1+743=744, 17+43=60, 174+3=177이므로, 셋 중 가장 작은 값은 60이 된다.
#  성재의 계산기 화면에 있는 숫자들을 나타낸 문자열이 주어질 때, 이와 같이 중간에 누락된 ‘+’ 하나를 넣었을 때의 결과 값의 최솟값을 구하는 프로그램을 작성하라.

#그리디 방식으로 접근했다. 인덱스 0부터 끝까지 나누면서 어느 부분일 때 최소값인지 비교해가며, 답을 도출
T = int(input())
for test_case in range(T):
    h = input()
    for t in range(1,len(h)):
        a=int(h[:t])
        b=int(h[t:])
        sum=a+b
        if(t==1): #처음에는 비교할 값이 없으니, 넣어줌
            min=sum
        if(sum<min): #그 다음 t가 1부터 비교할 수 있게 하는 if문을 나타냄
            min=sum
    print("#{0}".format(test_case+1), min)