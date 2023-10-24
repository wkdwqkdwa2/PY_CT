# 9자리 이하의 음이 아닌 정수 N이 있다. (미해결 문제)
# 당신은 이 수에서 한 쌍의 숫자를 골라 그 위치를 바꾸는 일을 최대 한 번 하여(안 하거나, 한 번만 하여) 새로운 수 M을 만들 수 있다. 단, 바꾼 결과 M의 맨 앞에 ‘0’이 나타나면 안 된다.

T=int(input())

for tc in range(T):
    ls=[]
    Number=input()
    ls.extend(Number)
    mx=sorted(ls,reverse=True) #내림차순
    mi=sorted(ls,reverse=False) #오름차순
    if(mi[0]=='0'):
        mi[0],mi[len(mi)-1]=mi[len(mi)-1],mi[0]
    print("#{} {} {}".format(tc+1,''.join(mi),''.join(mx)))