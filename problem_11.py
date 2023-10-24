T=int(input())

for tc in range(T):
    S=input()
    p_boll=0 #온전히 보이는 공의 개수
    for boll in range(1,len(S)):
        if(S[boll-1]=='(' and S[boll]==')'):
            p_boll+=1
    total=S.count('(')+S.count(')')-p_boll
    print("#{} {}".format(tc+1, total))