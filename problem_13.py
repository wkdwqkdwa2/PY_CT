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