T=int(input())
ls=[]
for tc in range(T):
    a=int(input())
    ls.append(a)
ls.sort()
for tc in ls:
    print(tc)