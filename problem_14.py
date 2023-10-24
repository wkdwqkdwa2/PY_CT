T=int(input())

for tc in range(T):
    mi_list=[]
    mx_list=[]
    
    Num=input()
    Mx=max(Num)
    Mi=min(Num)
    mx_index=Num.index(Mx)
    mi_index=Num.index(Mi)
    mi_list.extend(Num)
    mx_list.extend(Num)
    #최소값
    
    if(mi_list[mx_index]=='1'):
        mi_list[mx_index],mi_list[0]=mi_list[0],mi_list[mi_index]
    elif(mi_index!=0):
        mi_list[mi_index],mi_list[0]=mi_list[0],mi_list[mi_index]
   

    if(mx_index!=0):
        mx_list[mx_index],mx_list[0]=mx_list[0],mx_list[mx_index]
    print("#{} {} {}".format(tc+1,mi_list,mx_list))