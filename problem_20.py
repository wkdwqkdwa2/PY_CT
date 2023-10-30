T=int(input())

S=["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
for tc in range(T):
    day=input()
    
    ans=6-S.index(day)
    if ans==0:
        ans=7

    print("#{} {}".format(tc+1, ans))