T=int(input())

ls=list(map(int,input().split()))
ls.sort()
Sum=0
Sum_ls=[]
for tc in range(T):
    if tc==0:
        Sum=ls[tc]
        Sum_ls.append(Sum)
    else:
        Sum=Sum+ls[tc]
        Sum_ls.append(Sum)

print(sum(Sum_ls))