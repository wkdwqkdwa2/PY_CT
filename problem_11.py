#잡초는 ‘|’로 표현이며, 초원 '.', 공은'()'이다. 공은 가려져 있을 수 있으며, 공의 최솟값을 구해라.
T=int(input())

for tc in range(T):
    S=input()
    p_boll=0 #온전히 보이는 공의 개수
    for boll in range(1,len(S)):
        if(S[boll-1]=='(' and S[boll]==')'): #온전히 '()'모양인 것 경우를 나타낸다.
            p_boll+=1
    total=S.count('(')+S.count(')')-p_boll#떨어져 있는 '('와 ')'를 하나로 계산하고, 온전히 다 보이는 공의 갯수를 구하면 최솟값이다.
    print("#{} {}".format(tc+1, total))