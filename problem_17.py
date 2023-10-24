T=int(input())

for tc in range(T):
    A=input()
    li=[]
    li.extend(A)
    li.sort()
   
    if(li[0]==li[1] and li[2]==li[3] and li[0]!=li[2]):
        print("#{} Yes".format(tc+1))
    else:
        print("#{} No".format(tc+1))