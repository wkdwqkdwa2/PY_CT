#1206 swea

#빌딩의 기준을 바타으로 왼쪽과 오른쪽 2칸씩 총 4칸을 기준으로 전체적으로 높은 층들의 갯수

for test_case in range(1,11):
    B_len=int(input())
    building=list(map(int,input().split()))
    ans=0
    for i in range(2,B_len-2):    
        max_b=max(building[i-1],building[i-2],building[i+1],building[i+2])
        if building[i]-max_b>0:
            ans+=building[i]-max_b

    print("#{} {}".format(test_case,ans))      