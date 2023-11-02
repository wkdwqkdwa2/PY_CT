T=int(input())

for Tc in range(T):
    A=int(input()) #교육받을 횟수
    B=input().split() #교육 가능한 요일
    count=0
    day=0
    all_day=0
    while count!=A:
        if B[day]=='1':
            count+=1
            all_day+=1                    
            day+=1
            
            if day==7: day=0
        elif B[day]=='0':
            day+=1            
            all_day+=1                       
            if day==7: day=0
    if B[0]=='1':
        print("#{} {}".format(Tc+1,all_day))
    else:
        print("#{} {}".format(Tc+1,all_day-1))
    